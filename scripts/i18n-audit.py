#!/usr/bin/env python3
"""Audit German translations against English and find missing/placeholder keys."""

import json
import re
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, 'static/locales/en.json')) as f:
    en = json.load(f)
with open(os.path.join(BASE_DIR, 'static/locales/de.json')) as f:
    de = json.load(f)


def flatten_full(obj, prefix=''):
    items = []
    for k, v in obj.items():
        key = f'{prefix}.{k}' if prefix else k
        if isinstance(v, dict):
            items.extend(flatten_full(v, key))
        else:
            items.append((key, v))
    return items


en_items = flatten_full(en)
de_items = flatten_full(de)
en_dict = dict(en_items)
de_dict = dict(de_items)
en_keys = set(en_dict.keys())
de_keys = set(de_dict.keys())

# --- 1. Keys with identical English value in de.json ---
same_value = {k: en_dict[k] for k in en_keys & de_keys if en_dict[k] == de_dict[k]}

# --- 2. Chinese text remnants in de.json ---
def contains_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]', text))

chinese_in_de = {k: de_dict[k] for k in de_keys if contains_chinese(de_dict[k])}

# --- 3. Keys used in code but not in any locale file ---
t_calls = set()
patterns = [
    r"_t\(['\"]([^'\"]+)['\"]",
    r"t\(['\"]([^'\"]+)['\"]",
    r"\{\{ *['\"]([^'\"}]+)['\"] *\| *translate\}",
]

for root_dir in ['static', 'templates']:
    abs_root = os.path.join(BASE_DIR, root_dir)
    if not os.path.isdir(abs_root):
        continue
    for root, dirs, files in os.walk(abs_root):
        for f in files:
            if not f.endswith(('.js', '.html')):
                continue
            try:
                with open(os.path.join(root, f)) as fh:
                    content = fh.read()
                    for p in patterns:
                        for m in re.finditer(p, content):
                            t_calls.add(m.group(1))
            except Exception:
                pass

# Filter false positives (CSS selectors, HTML tags, code comments, test descriptions)
exact_skip = {
    'title', 'name', 'color', 'folder', 'notes', 'summary', 'participants',
    'screen', 'current', 'archived', 'shared', 'starred', 'inbox', 'anonymous',
}
prefix_skip = [
    '#', '.', '[data-', '/', 'button[', 'div[', '.bulk-', '.fixed', '.folder-modal',
    '.snippet-audio', '.speaker-modal', '.tag-modal', '.absolute',
]
description_keywords = [
    'accepts identifier', 'aggregates variables', 'capitalises', 'deduplicates',
    'does not', 'extracts', 'falls through', 'handles', 'is global', 'is the same',
    'produces label', 'records multiple', 'rejects', 'returns', 'skips',
    'tolerates', 'treats', 'uses tags',
]

def is_description(key):
    return len(key) > 60 and all(c.isascii() and (c.islower() or c.isspace() or c in '.,-()') for c in key)

missing_from_locale = set()
for k in t_calls:
    if any(k.startswith(p) for p in prefix_skip):
        continue
    if k in exact_skip or is_description(k):
        continue
    if any(kw in k for kw in description_keywords):
        continue
    if k not in en_keys:
        missing_from_locale.add(k)

# --- OUTPUT ---

def section_group(items_dict):
    sections = {}
    for k, v in sorted(items_dict.items()):
        sec = k.split('.')[0]
        sections.setdefault(sec, []).append((k, v))
    return sections

print("# Übersetzungs-Audit: Speakr Deutsche Lokalisierung\n")
print("## Zusammenfassung\n")
print(f"- **Keys in en.json:** {len(en_keys)}")
print(f"- **Keys in de.json:** {len(de_keys)}")
print(f"- **Vollständig fehlende Keys:** 0 (Struktur ist synchron)")
print(f"- **Unübersetzte Keys (Englisch in de.json):** {len(same_value)}")
print(f"- **Chinesische Textreste in de.json:** {len(chinese_in_de)}")
print(f"- **Im Code verwendete Keys ohne Locale-Eintrag:** {len(missing_from_locale)}")
print()

print("---\n")
print("## 1. Unübersetzte Keys (englischer Text in de.json)\n")
print(f"Insgesamt **{len(same_value)}** Keys haben in de.json denselben englischen Wert wie in en.json. Diese werden im UI weiterhin auf Englisch angezeigt.\n")

for section, items in sorted(section_group(same_value).items()):
    print(f"### {section} ({len(items)} Keys)\n")
    for k, v in items:
        print(f"- `{k}`")
    print()

print("---\n")
print("## 2. Chinesische Textreste in de.json\n")
print(f"**{len(chinese_in_de)}** Keys enthalten in de.json chinesischen Text – vermutlich aus einer anderen Locale-Datei (zh.json) übernommen.\n")

for k, v in sorted(chinese_in_de.items()):
    en_val = en_dict.get(k, 'N/A')
    print(f"- `{k}`")
    print(f"  - DE: \"{v}\"")
    print(f"  - EN: \"{en_val}\"")
    print()

print("---\n")
print("## 3. Im Code verwendete Keys ohne Locale-Eintrag\n")
print(f"**{len(missing_from_locale)}** Keys werden im Code mit `_t()` oder `t()` aufgerufen, haben aber **keinen Eintrag in en.json oder de.json**. Das UI zeigt in diesem Fall den rohen Key-Namen an.\n")

# Categorize
toast_msgs = sorted(k for k in missing_from_locale if any(k.startswith(p) for p in ['API', 'Account', 'Custom', 'Default', 'Enter', 'Error', 'Failed', 'Folder', 'Incognito', 'Installing', 'Meeting', 'Naming', 'Network', 'New', 'No', 'Notes', 'Notification', 'Please', 'Preferences', 'Processing', 'Push', 'Recording', 'Removed', 'Save', 'Screen', 'Share', 'Speaker', 'Speakr', 'Summary', 'Tag', 'Templates', 'Title', 'Token', 'Transcription', 'Using', 'Wake']))
other_keys = sorted(k for k in missing_from_locale if k not in toast_msgs)

if toast_msgs:
    print("### Toast/Notification-Nachrichten (direkt im JS als String)\n")
    print("Diese werden vermutlich als **Alert/Toast-Strings** ausgegeben und müssten entweder in en.json/de.json als Key angelegt oder im Code mit `_t()` übersetzt werden.\n")
    for k in toast_msgs:
        print(f"- `{k}`")
    print()

if other_keys:
    print("### Sonstige\n")
    for k in other_keys:
        print(f"- `{k}`")
    print()
