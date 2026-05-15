#!/usr/bin/env python3
"""
Translate all untranslated keys in de.json from English to German.
Also fixes Chinese text remnants and adds missing keys from en.json.

Run: python3 scripts/translate_de.py
This will output a translation table and modify de.json in place.
"""

import json
import re
import os
import copy
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DE_PATH = os.path.join(BASE_DIR, 'static/locales/de.json')
EN_PATH = os.path.join(BASE_DIR, 'static/locales/en.json')

with open(EN_PATH) as f:
    en = json.load(f)
with open(DE_PATH) as f:
    de = json.load(f)

def flatten(obj, prefix=''):
    items = []
    for k, v in obj.items():
        key = f'{prefix}.{k}' if prefix else k
        if isinstance(v, dict):
            items.extend(flatten(v, key))
        else:
            items.append((key, v))
    return items

def unflatten(items):
    """Convert flat key-value pairs back to nested dict."""
    result = {}
    for key, value in items:
        parts = key.split('.')
        current = result
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value
    return result

def set_nested(obj, key, value):
    """Set a value in a nested dict using dot notation."""
    parts = key.split('.')
    current = obj
    for part in parts[:-1]:
        if part not in current:
            current[part] = {}
        current = current[part]
    current[parts[-1]] = value

def get_nested(obj, key):
    """Get a value from a nested dict using dot notation."""
    parts = key.split('.')
    current = obj
    for part in parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return None
    return current

en_items = dict(flatten(en))
de_items = dict(flatten(de))

# ===== GERMAN TRANSLATIONS =====
# All untranslated keys with their German translations
translations = {
    # --- aboutPage ---
    "aboutPage.backend": "Backend",
    "aboutPage.dockerHub": "Docker Hub",
    "aboutPage.frontend": "Frontend",
    "aboutPage.githubRepository": "GitHub-Repository",
    "aboutPage.version": "Version",
    "aboutPage.whisperApi": "Whisper-API",

    # --- aboutPageDetails ---
    "aboutPageDetails.backend": "Backend",
    "aboutPageDetails.frontend": "Frontend",

    # --- account ---
    "account.autoLabel": "Auto-Beschriftung",
    "account.autoSummarizationDisabled": "Auto-Zusammenfassung von Admin deaktiviert",
    "account.autoSummarize": "Auto-Zusammenfassen",
    "account.defaultHotwords": "Standard-Hotwords",
    "account.defaultHotwordsPlaceholder": "z. B. Speakr, CTranslate2, PyAnnote, SDRs",
    "account.defaultInitialPrompt": "Standard-Initial-Prompt",
    "account.defaultInitialPromptPlaceholder": "z. B. Dies ist ein Meeting über KI-Transkriptionstools. Die Sprecher diskutieren über CTranslate2, PyAnnote und SDRs.",
    "account.personalFolder": "Persönlicher Ordner (nicht mit einer Gruppe verknüpft)",
    "account.personalTag": "Persönlicher Tag (nicht mit einer Gruppe verknüpft)",
    "account.ssoLinkAccount": "{{provider}}-Konto verknüpfen",
    "account.ssoLinked": "Verknüpft",
    "account.ssoNotLinked": "Nicht verknüpft",
    "account.ssoProvider": "Anbieter",
    "account.ssoSetPasswordFirst": "Zum Entkoppeln von SSO müssen Sie zuerst ein Passwort festlegen.",
    "account.ssoSubject": "Betreff:",
    "account.ssoUnlinkAccount": "{{provider}}-Konto entkoppeln",
    "account.ssoUnlinkConfirm": "Sind Sie sicher, dass Sie Ihr SSO-Konto entkoppeln möchten? Sie müssen dann Ihr Passwort zum Einloggen verwenden.",
    "account.transcriptionHints": "Transkriptionshinweise",
    "account.transcriptionHintsDesc": "Diese Standardwerte werden verwendet, wenn keine Tag- oder Ordner-Überschreibungen gesetzt sind. Sie helfen, die Transkriptionsgenauigkeit für Ihren spezifischen Anwendungsfall zu verbessern.",

    # --- adminDashboard ---
    "adminDashboard.admin": "ADMIN",
    "adminDashboard.allowed": "Erlaubt",
    "adminDashboard.createFirstGroup": "Erste Gruppe erstellen",
    "adminDashboard.created": "Erstellt",
    "adminDashboard.description": "Beschreibung",
    "adminDashboard.groupName": "Gruppenname",
    "adminDashboard.groupsTab": "Gruppen",
    "adminDashboard.id": "ID",
    "adminDashboard.megabytes": "MB",
    "adminDashboard.members": "Mitglieder",
    "adminDashboard.membersCount": "Mitglieder",
    "adminDashboard.noDescription": "Keine Beschreibung",
    "adminDashboard.noGroupsAdmin": "Sie sind noch kein Admin einer Gruppe",
    "adminDashboard.noGroupsCreated": "Noch keine Gruppen erstellt",
    "adminDashboard.noMembersYet": "Noch keine Mitglieder",
    "adminDashboard.passwordsDoNotMatch": "Passwörter stimmen nicht überein",
    "adminDashboard.publicShare": "Öffentliches Teilen",

    # --- buttons ---
    "buttons.cancel": "Abbrechen",
    "buttons.close": "Schließen",
    "buttons.createTag": "Tag erstellen",
    "buttons.deleteAll": "Alle löschen",
    "buttons.refresh": "Aktualisieren",
    "buttons.saveCustomPrompt": "Benutzerdefinierten Prompt speichern",
    "buttons.updateTag": "Tag aktualisieren",

    # --- chat ---
    "chat.cannotChatTranscriptionFailed": "Chat nicht möglich: Transkription fehlgeschlagen. Bitte transkribieren Sie die Aufnahme erneut.",
    "chat.cleared": "Chat geleert",
    "chat.downloadFailed": "Download des Chats fehlgeschlagen",
    "chat.downloadSuccess": "Chat erfolgreich heruntergeladen!",
    "chat.noMessagesToDownload": "Keine Chat-Nachrichten zum Herunterladen.",
    "chat.title": "Chat",

    # --- colorScheme ---
    "colorScheme.descriptions.amber": "Warme Bernsteintöne für ein gemütliches, produktives Gefühl",
    "colorScheme.descriptions.blue": "Klassisches Blau-Design mit einem sauberen, professionellen Look",
    "colorScheme.descriptions.emerald": "Naturinspiriertes Grün-Design für ein beruhigendes Erlebnis",
    "colorScheme.descriptions.purple": "Reichhaltiges Lila-Design mit einem eleganten, modernen Look",
    "colorScheme.descriptions.rose": "Warmes Rosen-Design mit einer sanften, einladenden Ästhetik",
    "colorScheme.descriptions.teal": "Kühles Türkis-Design mit einem erfrischenden, modernen Stil",
    "colorScheme.names.amber": "Goldener Bernstein",
    "colorScheme.names.blue": "Ozeanblau",
    "colorScheme.names.emerald": "Waldgrün",
    "colorScheme.names.purple": "Königspurpur",
    "colorScheme.names.rose": "Korallenrose",
    "colorScheme.names.teal": "Arktistürkis",

    # --- common ---
    "common.filter": "Filter",
    "common.info": "Info",
    "common.ok": "OK",

    # --- editTagModal ---
    "editTagModal.defaultPromptPlaceholder": "Leer lassen, um Ihren Standard-Zusammenfassungs-Prompt zu verwenden",
    "editTagModal.watchFolder": "Überwachungsordner",
    "editTagModal.watchFolderCreated": "Überwachungsordner erstellt",
    "editTagModal.watchFolderError": "Überwachungsordner konnte nicht erstellt werden",
    "editTagModal.watchFolderGroupTagError": "Überwachungsordner sind für Gruppen-Tags nicht verfügbar",
    "editTagModal.watchFolderPath": "Dateien ablegen in:",
    "editTagModal.watchFolderRemoved": "Überwachungsordner entfernt",

    # --- errors (59 keys, many still English) ---
    "errors.audioExtractionFailed": "Audio-Extraktion fehlgeschlagen",
    "errors.audioExtractionFailedGuidance": "Versuchen Sie, die Datei vor dem Hochladen in ein Standard-Audioformat (MP3, WAV) zu konvertieren.",
    "errors.audioExtractionFailedMessage": "Audio konnte nicht aus der hochgeladenen Datei extrahiert werden.",
    "errors.audioRecordingFailed": "Audioaufnahme fehlgeschlagen. Bitte überprüfen Sie Ihr Mikrofon.",
    "errors.authenticationError": "Authentifizierungsfehler",
    "errors.authenticationErrorGuidance": "Bitte überprüfen Sie, ob der API-Schlüssel korrekt und nicht abgelaufen ist.",
    "errors.authenticationErrorMessage": "Der Transkriptionsdienst hat die API-Anmeldedaten abgelehnt.",
    "errors.checkApiKeyGuidance": "API-Schlüssel in den Einstellungen überprüfen",
    "errors.checkNetworkGuidance": "Netzwerkverbindung überprüfen",
    "errors.connectionError": "Verbindungsfehler",
    "errors.connectionErrorGuidance": "Überprüfen Sie Ihre Internetverbindung und stellen Sie sicher, dass der Dienst verfügbar ist.",
    "errors.connectionErrorMessage": "Konnte keine Verbindung zum Transkriptionsdienst herstellen.",
    "errors.convertFormatGuidance": "Vor dem Hochladen in MP3 oder WAV konvertieren",
    "errors.convertStandardGuidance": "In ein Standard-Audioformat konvertieren",
    "errors.enableChunkingGuidance": "Chunking in den Einstellungen aktivieren oder die Datei komprimieren",
    "errors.fallbackMessage": "Ein Fehler ist aufgetreten",
    "errors.fallbackTitle": "Fehler",
    "errors.fileTooLarge": "Datei zu groß",
    "errors.fileTooLargeGuidance": "Versuchen Sie, Audio-Chunking in Ihren Einstellungen zu aktivieren oder die Audiodatei vor dem Hochladen zu komprimieren.",
    "errors.fileTooLargeMaxSize": "Datei zu groß. Max: {{size}} MB.",
    "errors.fileTooLargeMessage": "Die Audiodatei überschreitet die vom Transkriptionsdienst zugelassene Maximalgröße.",
    "errors.fileTooLargeTitle": "Datei zu groß",
    "errors.generic": "Ein Fehler ist aufgetreten",
    "errors.invalidAudioFormat": "Ungültiges Audioformat",
    "errors.invalidAudioFormatGuidance": "Versuchen Sie, die Audiodatei vor dem Hochladen in MP3 oder WAV zu konvertieren.",
    "errors.invalidAudioFormatMessage": "Das Audioformat wird nicht unterstützt oder die Datei ist möglicherweise beschädigt.",
    "errors.networkError": "Netzwerkfehler. Bitte überprüfen Sie Ihre Verbindung.",
    "errors.networkErrorDuringUpload": "Netzwerkfehler während des Uploads",
    "errors.notFound": "Nicht gefunden",
    "errors.permissionDenied": "Zugriff verweigert",
    "errors.processingError": "Verarbeitungsfehler",
    "errors.processingErrorFallbackGuidance": "Versuchen Sie, die Aufnahme erneut zu verarbeiten",
    "errors.processingErrorGuidance": "Wenn dieser Fehler weiterhin besteht, versuchen Sie, die Aufnahme erneut zu verarbeiten.",
    "errors.processingErrorMessage": "Während der Verarbeitung ist ein Fehler aufgetreten.",
    "errors.processingFailedOnServer": "Verarbeitung auf dem Server fehlgeschlagen.",
    "errors.processingFailedWithStatus": "Verarbeitung mit Status {{status}} fehlgeschlagen",
    "errors.processingTimeout": "Verarbeitungszeitüberschreitung",
    "errors.processingTimeoutGuidance": "Dies kann bei sehr langen Aufnahmen passieren. Versuchen Sie, die Audiodatei in kleinere Teile aufzuteilen.",
    "errors.processingTimeoutMessage": "Die Transkription hat zu lange gedauert.",
    "errors.quotaExceeded": "Speicherkontingent überschritten",
    "errors.rateLimitExceeded": "Ratenlimit überschritten",
    "errors.rateLimitExceededGuidance": "Bitte warten Sie einige Minuten und versuchen Sie es erneut.",
    "errors.rateLimitExceededMessage": "Es wurden zu viele Anfragen an den Transkriptionsdienst gesendet.",
    "errors.serverErrorStatus": "Serverfehler ({{status}})",
    "errors.serviceUnavailable": "Dienst nicht verfügbar",
    "errors.serviceUnavailableGuidance": "Dies ist normalerweise vorübergehend. Bitte versuchen Sie es in ein paar Minuten erneut.",
    "errors.serviceUnavailableMessage": "Der Transkriptionsdienst ist vorübergehend nicht verfügbar.",
    "errors.splitAudioGuidance": "Versuchen Sie, die Audiodatei in kleinere Teile aufzuteilen",
    "errors.summaryFailed": "Zusammenfassung fehlgeschlagen. Bitte versuchen Sie es erneut.",
    "errors.transcriptionFailed": "Transkription fehlgeschlagen. Bitte versuchen Sie es erneut.",
    "errors.tryAgainLaterGuidance": "Versuchen Sie es in ein paar Minuten erneut",
    "errors.unauthorized": "Nicht autorisiert",
    "errors.unexpectedResponse": "Unerwartete Erfolgsantwort vom Server nach dem Upload.",
    "errors.unsupportedFormat": "Nicht unterstütztes Format",
    "errors.uploadFailed": "Upload fehlgeschlagen. Bitte versuchen Sie es erneut.",
    "errors.uploadFailedWithStatus": "Upload mit Status {{status}} fehlgeschlagen",
    "errors.uploadTimedOut": "Upload-Zeitüberschreitung",
    "errors.validationError": "Validierungsfehler",
    "errors.waitAndRetryGuidance": "Einige Minuten warten und erneut versuchen",

    # --- exportLabels ---
    "exportLabels.tags": "Tags",

    # --- exportTemplates ---
    "exportTemplates.tabTitle": "Export",

    # --- fileSize ---
    "fileSize.bytes": "{{count}} B",
    "fileSize.gigabytes": "{{count}} GB",
    "fileSize.kilobytes": "{{count}} KB",
    "fileSize.megabytes": "{{count}} MB",

    # --- form ---
    "form.auto": "Auto",
    "form.folder": "Ordner",
    "form.hotwords": "Hotwords",
    "form.hotwordsHelp": "Durch Komma getrennte Wörter zur Verbesserung der Erkennung domänenspezifischer Begriffe",
    "form.hotwordsPlaceholder": "z. B. Speakr, CTranslate2, PyAnnote",
    "form.initialPrompt": "Initial-Prompt",
    "form.initialPromptHelp": "Kontext zur Steuerung des Stils und Vokabulars des Transkriptionsmodells",
    "form.initialPromptPlaceholder": "z. B. Dies ist ein Meeting über KI-Transkriptionstools.",
    "form.optional": "Optional",
    "form.participantNamePlaceholder": "Teilnehmername...",
    "form.placeholderAuto": "Auto",
    "form.placeholderOptional": "Optional",
    "form.transcriptionLanguage": "Transkriptionssprache",

    # --- help ---
    "help.allTagsSelected": "Alle Tags ausgewählt",
    "help.autoIdentifyMobile": "Auto",
    "help.createFolders": "Ordner erstellen",
    "help.defaultHotwordsHelp": "Durch Komma getrennte Wörter oder Phrasen, die das Transkriptionsmodell priorisieren soll.",
    "help.defaultInitialPromptHelp": "Kontext zur Steuerung des Stils und Vokabulars des Transkriptionsmodells. Beschreiben Sie das Thema für bessere Ergebnisse.",
    "help.dragToReorder": "Zum Umsortieren ziehen",
    "help.firstTagAsrSettings": "ASR-Einstellungen des ersten Tags werden angewendet:",
    "help.firstTagDefaultsApplied": "Standardeinstellungen des ersten Tags angewendet",
    "help.folderHasCustomPrompt": "Dieser Ordner hat einen benutzerdefinierten Zusammenfassungs-Prompt",
    "help.noMatchingTags": "Keine passenden Tags",
    "help.selectedTagsCustomPrompts": "Ausgewählte Tags enthalten benutzerdefinierte Zusammenfassungs-Prompts",
    "help.startTime": "Start",
    "help.toOrganizeRecordings": "um Ihre Aufnahmen zu organisieren",

    # --- incognito ---
    "incognito.audioNotStored": "Audio wird im Inkognito-Modus nicht gespeichert",
    "incognito.discardConfirm": "Dadurch wird Ihre Inkognito-Aufnahme endgültig verworfen. Fortfahren?",
    "incognito.mode": "Inkognito-Modus",
    "incognito.notSavedToAccount": "Nicht im Konto gespeichert",
    "incognito.oneFileAtATime": "Der Inkognito-Modus unterstützt nur eine Datei gleichzeitig",
    "incognito.processInIncognito": "Inkognito verarbeiten",
    "incognito.processWithoutSaving": "Ohne Speichern verarbeiten",
    "incognito.processing": "Verarbeitung läuft...",
    "incognito.processingComplete": "Verarbeitung abgeschlossen!",
    "incognito.processingInProgress": "Verarbeitung im Inkognito-Modus...",
    "incognito.recordingDiscarded": "Inkognito-Aufnahme verworfen",
    "incognito.recordingProcessed": "Inkognito-Aufnahme verarbeitet – Daten gehen beim Schließen des Tabs verloren",
    "incognito.recordingReady": "Inkognito-Aufnahme bereit!",
    "incognito.recordingTitle": "Inkognito-Aufnahme",
    "incognito.selectExactlyOneFile": "Wählen Sie genau eine Datei aus",
    "incognito.sessionOnly": "Nur für diese Sitzung",
    "incognito.uploadingFile": "Datei wird für Inkognito-Verarbeitung hochgeladen...",

    # --- inquire ---
    "inquire.tags": "Tags",

    # --- languages ---
    "languages.hi": "Hindi",

    # --- messages ---
    "messages.colorSchemeApplied": "Farbschema angewendet",
    "messages.colorSchemeReset": "Farbschema auf Standard zurückgesetzt",
    "messages.copiedSuccessfully": "In die Zwischenablage kopiert!",
    "messages.copyFailed": "Kopieren fehlgeschlagen",
    "messages.copyNotSupported": "Kopieren fehlgeschlagen. Ihr Browser unterstützt diese Funktion möglicherweise nicht.",
    "messages.errorRecoveringRecording": "Fehler beim Wiederherstellen der Aufnahme",
    "messages.eventDownloadFailed": "Download des Ereignisses fehlgeschlagen",
    "messages.eventDownloadSuccess": "Ereignis \"{{title}}\" heruntergeladen. Öffnen Sie die Datei, um sie zu Ihrem Kalender hinzuzufügen.",
    "messages.eventsExportFailed": "Export der Ereignisse fehlgeschlagen",
    "messages.eventsExportSuccess": "{{count}} Ereignisse exportiert",
    "messages.failedToDeleteJob": "Löschen des Auftrags fehlgeschlagen",
    "messages.failedToRecoverRecording": "Wiederherstellen der Aufnahme fehlgeschlagen",
    "messages.failedToRetryJob": "Wiederholen des Auftrags fehlgeschlagen",
    "messages.failedToSave": "Speichern fehlgeschlagen: {{error}}",
    "messages.failedToSaveParticipants": "Speichern der Teilnehmer fehlgeschlagen",
    "messages.followPlayerDisabled": "Follow-Player-Modus deaktiviert",
    "messages.followPlayerEnabled": "Follow-Player-Modus aktiviert",
    "messages.invalidEventData": "Ungültige Ereignisdaten",
    "messages.jobQueuedForRetry": "Auftrag zur Wiederholung eingereiht",
    "messages.noEventsToExport": "Keine Ereignisse zum Exportieren",
    "messages.noNotesAvailableDownload": "Keine Notizen zum Herunterladen verfügbar.",
    "messages.noNotesToCopy": "Keine Notizen zum Kopieren verfügbar.",
    "messages.noPermissionToEdit": "Sie haben keine Berechtigung, diese Aufnahme zu bearbeiten",
    "messages.noSummaryToCopy": "Keine Zusammenfassung zum Kopieren verfügbar.",
    "messages.noSummaryToDownload": "Keine Zusammenfassung zum Herunterladen verfügbar.",
    "messages.noTranscriptionToCopy": "Keine Transkription zum Kopieren verfügbar.",
    "messages.noTranscriptionToDownload": "Keine Transkription zum Herunterladen verfügbar.",
    "messages.notesCopied": "Notizen in die Zwischenablage kopiert!",
    "messages.notesDownloadFailed": "Download der Notizen fehlgeschlagen",
    "messages.notesDownloadSuccess": "Notizen erfolgreich heruntergeladen!",
    "messages.recordingDiscarded": "Aufnahme verworfen",
    "messages.recordingRecovered": "Aufnahme erfolgreich wiederhergestellt",
    "messages.saveParticipantsFailed": "Speichern fehlgeschlagen: {{error}}",
    "messages.summaryCopied": "Zusammenfassung in die Zwischenablage kopiert!",
    "messages.summaryDownloadFailed": "Download der Zusammenfassung fehlgeschlagen",
    "messages.summaryDownloadSuccess": "Zusammenfassung erfolgreich heruntergeladen!",
    "messages.transcriptDownloadFailed": "Download des Transkripts fehlgeschlagen",
    "messages.transcriptDownloadSuccess": "Transkript erfolgreich heruntergeladen!",
    "messages.transcriptionCopied": "Transkription in die Zwischenablage kopiert!",

    # --- metadata ---
    "metadata.status": "Status",

    # --- recording ---
    "recording.micPlusSys": "Mikro + System",
    "recording.pauseRecording": "Pause",

    # --- sharing ---
    "sharing.teamBadge": "Gruppe",

    # --- sidebar ---
    "sidebar.starred": "Markiert",
    "sidebar.tags": "Tags",

    # --- tagManagement ---
    "tagManagement.maxSpeakers": "Max",
    "tagManagement.minSpeakers": "Min",

    # --- tags ---
    "tags.title": "Tags",

    # --- tooltips ---
    "tooltips.exitFullscreen": "Vollbild beenden",
    "tooltips.fullscreenVideo": "Video im Vollbild",
    "tooltips.hideVideo": "Video ausblenden",
    "tooltips.pause": "Pause",
    "tooltips.showVideo": "Video einblenden",

    # --- upload ---
    "upload.fileExceedsMaxSize": "Datei \"{{name}}\" überschreitet die maximale Größe von {{size}} MB und wurde übersprungen.",
    "upload.fileRemovedFromQueue": "Datei aus der Warteschlange entfernt",
    "upload.filesToUpload": "Dateien zum Hochladen",
    "upload.invalidFileType": "Ungültiger Dateityp \"{{name}}\". Nur Audiodateien und Video-Container mit Audio (MP3, WAV, M4A, MP4, WebM, OGG, FLAC) werden unterstützt.",
    "upload.settingsApplyToAll": "Einstellungen gelten für alle Dateien in dieser Sitzung",
    "upload.uploadNFiles": "{{count}} Datei(en) hochladen",

    # --- help.systemAudioHelp (sonstige Fehlende) ---
    "help.systemAudioHelp": "Systemaudio aufnehmen – wählen Sie diesen Eintrag in Ihrem Bildschirmfreigabefenster aus. Stellen Sie sicher, dass Sie \"Tab\" oder \"Bildschirm\" und nicht nur \"Ihren Bildschirm\" auswählen.",
}

# ===== Chinese text fixes =====
chinese_fixes = {
    "errors.audioRecordingFailed": "Audioaufnahme fehlgeschlagen. Bitte überprüfen Sie Ihr Mikrofon.",
    "errors.fileTooLarge": "Datei zu groß",
    "errors.generic": "Ein Fehler ist aufgetreten",
    "errors.networkError": "Netzwerkfehler. Bitte überprüfen Sie Ihre Verbindung.",
    "errors.notFound": "Nicht gefunden",
    "errors.permissionDenied": "Zugriff verweigert",
    "errors.quotaExceeded": "Speicherkontingent überschritten",
    "errors.summaryFailed": "Zusammenfassung fehlgeschlagen. Bitte versuchen Sie es erneut.",
    "errors.transcriptionFailed": "Transkription fehlgeschlagen. Bitte versuchen Sie es erneut.",
    "errors.unauthorized": "Nicht autorisiert",
    "errors.unsupportedFormat": "Nicht unterstütztes Format",
    "errors.uploadFailed": "Upload fehlgeschlagen. Bitte versuchen Sie es erneut.",
    "errors.validationError": "Validierungsfehler",
}

# ===== Missing keys from code (add to en.json and de.json) =====
# These are toast/notification messages used directly as strings in JS code
# We add them to both locale files so they can be translated
missing_keys = {
    # Toast/notification messages
    "toasts.apiTokenCreated": {"en": "API token created successfully", "de": "API-Token erfolgreich erstellt"},
    "toasts.accountUpdated": {"en": "Account information updated successfully", "de": "Kontoinformationen erfolgreich aktualisiert"},
    "toasts.customPromptSaved": {"en": "Custom prompt saved successfully", "de": "Benutzerdefinierter Prompt erfolgreich gespeichert"},
    "toasts.exportTemplateCreated": {"en": "Default export template created successfully", "de": "Standard-Exportvorlage erfolgreich erstellt"},
    "toasts.namingTemplateUpdated": {"en": "Default naming template updated", "de": "Standard-Benennungsvorlage aktualisiert"},
    "toasts.namingTemplatesCreated": {"en": "Default naming templates created", "de": "Standard-Benennungsvorlagen erstellt"},
    "toasts.defaultTemplatesCreated": {"en": "Default templates created successfully", "de": "Standardvorlagen erfolgreich erstellt"},
    "toasts.enterModelId": {"en": "Enter the model id (e.g. whisper-1, large-v3, voxtral-mini-latest):", "de": "Modell-ID eingeben (z. B. whisper-1, large-v3, voxtral-mini-latest):"},
    "toasts.errorDeletingShare": {"en": "Error deleting share.", "de": "Fehler beim Löschen der Freigabe."},
    "toasts.errorUpdatingShare": {"en": "Error updating share.", "de": "Fehler beim Aktualisieren der Freigabe."},
    "toasts.failedPushNotificationsConfig": {"en": "Failed to configure push notifications", "de": "Push-Benachrichtigungen konnten nicht konfiguriert werden"},
    "toasts.failedCopyToken": {"en": "Failed to copy token to clipboard", "de": "Token konnte nicht in die Zwischenablage kopiert werden"},
    "toasts.failedCreateExportTemplate": {"en": "Failed to create default export template", "de": "Standard-Exportvorlage konnte nicht erstellt werden"},
    "toasts.failedCreateNamingTemplates": {"en": "Failed to create default naming templates", "de": "Standard-Benennungsvorlagen konnten nicht erstellt werden"},
    "toasts.failedCreateTemplates": {"en": "Failed to create default templates", "de": "Standardvorlagen konnten nicht erstellt werden"},
    "toasts.failedCreateToken": {"en": "Failed to create token: ", "de": "Token konnte nicht erstellt werden: "},
    "toasts.failedDeleteExportTemplate": {"en": "Failed to delete export template", "de": "Exportvorlage konnte nicht gelöscht werden"},
    "toasts.failedDeleteFolder": {"en": "Failed to delete folder: ", "de": "Ordner konnte nicht gelöscht werden: "},
    "toasts.failedDeleteTemplate": {"en": "Failed to delete template", "de": "Vorlage konnte nicht gelöscht werden"},
    "toasts.failedDisablePush": {"en": "Failed to disable push notifications", "de": "Push-Benachrichtigungen konnten nicht deaktiviert werden"},
    "toasts.failedEnablePush": {"en": "Failed to enable push notifications", "de": "Push-Benachrichtigungen konnten nicht aktiviert werden"},
    "toasts.failedLoadExportTemplates": {"en": "Failed to load export templates", "de": "Exportvorlagen konnten nicht geladen werden"},
    "toasts.failedLoadNamingTemplates": {"en": "Failed to load naming templates", "de": "Benennungsvorlagen konnten nicht geladen werden"},
    "toasts.failedLoadTemplates": {"en": "Failed to load templates", "de": "Vorlagen konnten nicht geladen werden"},
    "toasts.failedRevokeToken": {"en": "Failed to revoke token: ", "de": "Token konnte nicht widerrufen werden: "},
    "toasts.failedSaveCustomPrompt": {"en": "Failed to save custom prompt", "de": "Benutzerdefinierter Prompt konnte nicht gespeichert werden"},
    "toasts.failedSaveFolder": {"en": "Failed to save folder: ", "de": "Ordner konnte nicht gespeichert werden: "},
    "toasts.failedSavePreferences": {"en": "Failed to save preferences", "de": "Einstellungen konnten nicht gespeichert werden"},
    "toasts.failedTestTemplate": {"en": "Failed to test template", "de": "Vorlage konnte nicht getestet werden"},
    "toasts.failedUpdateAccount": {"en": "Failed to update account information", "de": "Kontoinformationen konnten nicht aktualisiert werden"},
    "toasts.failedUpdateDefaultTemplate": {"en": "Failed to update default template", "de": "Standardvorlage konnte nicht aktualisiert werden"},
    "toasts.failedUpdateLanguage": {"en": "Failed to update language. Please try again.", "de": "Sprache konnte nicht aktualisiert werden. Bitte versuchen Sie es erneut."},
    "toasts.failedUpdateToken": {"en": "Failed to update token: ", "de": "Token konnte nicht aktualisiert werden: "},
    "toasts.folderNameRequired": {"en": "Folder name is required", "de": "Ordnername ist erforderlich"},
    "toasts.folderPrefix": {"en": "Folder ", "de": "Ordner "},
    "toasts.incognitoRecordingLost": {"en": "Incognito recording processed - data will be lost when tab closes", "de": "Inkognito-Aufnahme verarbeitet – Daten gehen beim Schließen des Tabs verloren"},
    "toasts.installingSpeakr": {"en": "Installing Speakr...", "de": "Speakr wird installiert..."},
    "toasts.meetingDateUpdated": {"en": "Meeting date updated!", "de": "Meeting-Datum aktualisiert!"},
    "toasts.namingTemplateDeleted": {"en": "Naming template deleted", "de": "Benennungsvorlage gelöscht"},
    "toasts.networkError": {"en": "Network error: ", "de": "Netzwerkfehler: "},
    "toasts.passwordMismatch": {"en": "New password and confirmation do not match.", "de": "Das neue Passwort und die Bestätigung stimmen nicht überein."},
    "toasts.noAudioTrack": {"en": "No audio track - check ", "de": "Keine Audiospur – überprüfen Sie "},
    "toasts.noSourceSpeakers": {"en": "No source speakers to merge", "de": "Keine Quell-Sprecher zum Zusammenführen"},
    "toasts.notesCopied": {"en": "Notes copied to clipboard!", "de": "Notizen in die Zwischenablage kopiert!"},
    "toasts.notesSavedBrowser": {"en": "Notes saved (in browser only)", "de": "Notizen gespeichert (nur im Browser)"},
    "toasts.notesSaved": {"en": "Notes saved!", "de": "Notizen gespeichert!"},
    "toasts.notificationDenied": {"en": "Notification permission denied", "de": "Benachrichtigungsberechtigung verweigert"},
    "toasts.notificationsEnabled": {"en": "Notifications enabled", "de": "Benachrichtigungen aktiviert"},
    "toasts.enterTokenName": {"en": "Please enter a token name", "de": "Bitte geben Sie einen Token-Namen ein"},
    "toasts.selectMinSpeakers": {"en": "Please select at least 2 speakers to merge", "de": "Bitte wählen Sie mindestens 2 Sprecher zum Zusammenführen aus"},
    "toasts.selectSpeakersClear": {"en": "Please select speakers to clear voice profiles", "de": "Bitte wählen Sie Sprecher zum Löschen der Sprachprofile aus"},
    "toasts.selectSpeakersDelete": {"en": "Please select speakers to delete", "de": "Bitte wählen Sie zu löschende Sprecher aus"},
    "toasts.selectSpeakerKeep": {"en": "Please select which speaker to keep", "de": "Bitte wählen Sie den zu behaltenden Sprecher aus"},
    "toasts.preferencesSaved": {"en": "Preferences saved", "de": "Einstellungen gespeichert"},
    "toasts.processingCompleted": {"en": "Processing completed!", "de": "Verarbeitung abgeschlossen!"},
    "toasts.processingFailed": {"en": "Processing failed", "de": "Verarbeitung fehlgeschlagen"},
    "toasts.pushDenied": {"en": "Push notification permission denied", "de": "Push-Benachrichtigungsberechtigung verweigert"},
    "toasts.pushDisabled": {"en": "Push notifications disabled", "de": "Push-Benachrichtigungen deaktiviert"},
    "toasts.pushEnabled": {"en": "Push notifications enabled", "de": "Push-Benachrichtigungen aktiviert"},
    "toasts.pushNotAvailable": {"en": "Push notifications not available. Install pywebpush on server.", "de": "Push-Benachrichtigungen nicht verfügbar. Installieren Sie pywebpush auf dem Server."},
    "toasts.pushNotSupported": {"en": "Push notifications not supported in this browser", "de": "Push-Benachrichtigungen werden in diesem Browser nicht unterstützt"},
    "toasts.recordingArchived": {"en": "Recording archived (audio deleted)", "de": "Aufnahme archiviert (Audio gelöscht)"},
    "toasts.recordingDeleted": {"en": "Recording deleted.", "de": "Aufnahme gelöscht."},
    "toasts.recordingReset": {"en": "Recording reset for reprocessing.", "de": "Aufnahme für erneute Verarbeitung zurückgesetzt."},
    "toasts.recordingResumed": {"en": "Recording resumed - screen will stay awake", "de": "Aufnahme fortgesetzt – Bildschirm bleibt wach"},
    "toasts.recordingStatusReset": {"en": "Recording status reset to FAILED", "de": "Aufnahmestatus auf FEHLGESCHLAGEN zurückgesetzt"},
    "toasts.recordingUpdated": {"en": "Recording updated!", "de": "Aufnahme aktualisiert!"},
    "toasts.removedFromFolder": {"en": "Removed from folder", "de": "Aus Ordner entfernt"},
    "toasts.saveTemplateFirst": {"en": "Save the template first to test it", "de": "Speichern Sie die Vorlage zuerst, um sie zu testen"},
    "toasts.screenLockDenied": {"en": "Screen lock permission denied", "de": "Bildschirmsperrberechtigung verweigert"},
    "toasts.screenMaySleep": {"en": "Screen may sleep during recording", "de": "Bildschirm kann während der Aufnahme in den Ruhezustand gehen"},
    "toasts.screenSharingCancelled": {"en": "Screen sharing was cancelled", "de": "Bildschirmfreigabe wurde abgebrochen"},
    "toasts.shareDeleted": {"en": "Share deleted successfully", "de": "Freigabe erfolgreich gelöscht"},
    "toasts.shareLinkCopied": {"en": "Share link copied to clipboard", "de": "Freigabelink in die Zwischenablage kopiert"},
    "toasts.shareLinkCreated": {"en": "Share link created successfully!", "de": "Freigabelink erfolgreich erstellt!"},
    "toasts.shareLinkDeleted": {"en": "Share link deleted successfully.", "de": "Freigabelink erfolgreich gelöscht."},
    "toasts.sharePermissionsUpdated": {"en": "Share permissions updated.", "de": "Freigabeberechtigungen aktualisiert."},
    "toasts.speakerNameUpdated": {"en": "Speaker name updated successfully", "de": "Sprechername erfolgreich aktualisiert"},
    "toasts.speakrInstalled": {"en": "Speakr installed successfully!", "de": "Speakr erfolgreich installiert!"},
    "toasts.summaryCopied": {"en": "Summary copied to clipboard!", "de": "Zusammenfassung in die Zwischenablage kopiert!"},
    "toasts.summaryGenerated": {"en": "Summary generated", "de": "Zusammenfassung erstellt"},
    "toasts.summaryGenerationStarted": {"en": "Summary generation started", "de": "Zusammenfassungserstellung gestartet"},
    "toasts.summaryReprocessingStarted": {"en": "Summary reprocessing started", "de": "Erneute Zusammenfassungserstellung gestartet"},
    "toasts.summarySaved": {"en": "Summary saved!", "de": "Zusammenfassung gespeichert!"},
    "toasts.tagAdded": {"en": "Tag added successfully", "de": "Tag erfolgreich hinzugefügt"},
    "toasts.tagAddedExcl": {"en": "Tag added!", "de": "Tag hinzugefügt!"},
    "toasts.tagRemoved": {"en": "Tag removed successfully", "de": "Tag erfolgreich entfernt"},
    "toasts.tagRemovedExcl": {"en": "Tag removed!", "de": "Tag entfernt!"},
    "toasts.tagsReordered": {"en": "Tags reordered", "de": "Tags neu angeordnet"},
    "toasts.exportTemplateDeleted": {"en": "Export template deleted successfully", "de": "Exportvorlage erfolgreich gelöscht"},
    "toasts.templateDeleted": {"en": "Template deleted successfully", "de": "Vorlage erfolgreich gelöscht"},
    "toasts.titleRegenerated": {"en": "Title regenerated", "de": "Titel neu generiert"},
    "toasts.tokenCopied": {"en": "Token copied to clipboard", "de": "Token in die Zwischenablage kopiert"},
    "toasts.tokenNameEmpty": {"en": "Token name cannot be empty", "de": "Token-Name darf nicht leer sein"},
    "toasts.tokenNameUpdated": {"en": "Token name updated", "de": "Token-Name aktualisiert"},
    "toasts.tokenRevoked": {"en": "Token revoked successfully", "de": "Token erfolgreich widerrufen"},
    "toasts.transcriptionCopied": {"en": "Transcription copied to clipboard!", "de": "Transkription in die Zwischenablage kopiert!"},
    "toasts.transcriptionReprocessingStarted": {"en": "Transcription reprocessing started", "de": "Erneute Transkription gestartet"},
    "toasts.transcriptionUpdated": {"en": "Transcription updated successfully!", "de": "Transkription erfolgreich aktualisiert!"},
    "toasts.usingExistingShareLink": {"en": "Using existing share link", "de": "Vorhandenen Freigabelink verwenden"},
    "toasts.wakeLockNotSupported": {"en": "Wake lock not supported on this device", "de": "Wake-Lock wird auf diesem Gerät nicht unterstützt"},
    "toasts.iOSWakeLockIssue": {"en": "iOS wake lock may not work - keep screen active", "de": "iOS Wake-Lock funktioniert möglicherweise nicht – Bildschirm aktiv halten"},
}

# Apply translations to de.json
changed_keys = []
already_translated = []
chinese_fixed = []

for key, de_translation in translations.items():
    current_de = get_nested(de, key)
    current_en = get_nested(en, key)
    if current_de == current_en:
        set_nested(de, key, de_translation)
        changed_keys.append((key, current_en, de_translation))
    elif current_de is None:
        set_nested(de, key, de_translation)
        changed_keys.append((key, f"[MISSING IN DE] {current_en}", de_translation))
    else:
        already_translated.append((key, current_de))

# Apply Chinese fixes (these also match translations above, so they're effectively already applied)
for key, de_translation in chinese_fixes.items():
    # Check if this was already overwritten by translations above
    current_de = get_nested(de, key)
    en_val = get_nested(en, key)
    if current_de and en_val and current_de != en_val:
        # Already translated by us, skip
        pass
    elif current_de and contains_chinese(current_de):
        set_nested(de, key, de_translation)
        chinese_fixed.append((key, current_de, de_translation))

def contains_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]', str(text)))

# Check for remaining Chinese text
remaining_chinese = []
for key in flatten(de):
    k, v = key
    if contains_chinese(v):
        remaining_chinese.append((k, v))

# Apply missing keys to en.json and de.json
missing_added = []
for key, langs in sorted(missing_keys.items()):
    parts = key.split('.')
    # Add to en.json
    en_current = en
    for part in parts[:-1]:
        if part not in en_current:
            en_current[part] = {}
        en_current = en_current[part]
    if parts[-1] not in en_current:
        en_current[parts[-1]] = langs['en']
        missing_added.append((key, langs['en'], langs['de']))
    # Add to de.json
    de_current = de
    for part in parts[:-1]:
        if part not in de_current:
            de_current[part] = {}
        de_current = de_current[part]
    if parts[-1] not in de_current:
        de_current[parts[-1]] = langs['de']

# Write the updated de.json and en.json
with open(DE_PATH, 'w', encoding='utf-8') as f:
    json.dump(de, f, indent=2, ensure_ascii=False)
    f.write('\n')
with open(EN_PATH, 'w', encoding='utf-8') as f:
    json.dump(en, f, indent=2, ensure_ascii=False)
    f.write('\n')

# ===== Generate README =====
readme = []
readme.append("# Übersetzungs-Änderungen (English → Deutsch)")
readme.append("")
readme.append("Dieses Dokument listet alle Übersetzungen auf, die in `de.json` vorgenommen wurden.")
readme.append("")
readme.append(f"**Durchgeführt am:** {__import__('datetime').datetime.now().strftime('%d.%m.%Y')}")
readme.append("")
readme.append("---")
readme.append("")

# Summary
readme.append("## Zusammenfassung")
readme.append("")
readme.append(f"- **Neu übersetzte Keys:** {len(changed_keys)}")
if chinese_fixed:
    readme.append(f"- **Korrigierte chinesische Textreste:** {len(chinese_fixed)}")
if remaining_chinese:
    readme.append(f"- **⚠️ Verbleibende chinesische Textreste:** {len(remaining_chinese)} (müssen manuell geprüft werden)")
if already_translated:
    readme.append(f"- **Bereits übersetzt (nicht geändert):** {len(already_translated)}")
readme.append("")
readme.append("---")
readme.append("")

# Section: New translations
readme.append("## Neue Übersetzungen")
readme.append("")
readme.append("| Key | Englisch (en.json) | Deutsch (de.json) |")
readme.append("|-----|-------------------|--------------------|")
for key, en_val, de_val in changed_keys:
    # Escape pipe characters in values
    en_escaped = str(en_val).replace('|', '\\|')
    de_escaped = str(de_val).replace('|', '\\|')
    readme.append(f"| `{key}` | {en_escaped} | {de_escaped} |")

readme.append("")

# Section: Chinese fixes
if chinese_fixed:
    readme.append("---")
    readme.append("")
    readme.append("## Korrigierte chinesische Textreste")
    readme.append("")
    readme.append("| Key | Vorher (Chinesisch) | Nachher (Deutsch) |")
    readme.append("|-----|--------------------|-------------------|")
    for key, old_val, new_val in chinese_fixed:
        old_escaped = str(old_val).replace('|', '\\|')
        new_escaped = str(new_val).replace('|', '\\|')
        readme.append(f"| `{key}` | {old_escaped} | {new_escaped} |")
    readme.append("")

# Section: Remaining Chinese
if remaining_chinese:
    readme.append("---")
    readme.append("")
    readme.append("## ⚠️ Verbleibende chinesische Textreste (manuelle Prüfung nötig)")
    readme.append("")
    readme.append("| Key | Aktueller Wert |")
    readme.append("|-----|---------------|")
    for key, val in remaining_chinese:
        val_escaped = str(val).replace('|', '\\|')
        readme.append(f"| `{key}` | {val_escaped} |")
    readme.append("")

# Section: Missing keys added to en.json and de.json
if missing_added:
    readme.append("---")
    readme.append("")
    readme.append("## Neu hinzugefügte Keys (für bisher unübersetzte JS-Strings)")
    readme.append("")
    readme.append(f"Folgende **{len(missing_added)} Keys** wurden zu `en.json` **und** `de.json` hinzugefügt, da sie im Code als direkte Strings verwendet wurden.")
    readme.append("")
    readme.append("| Key | Englisch | Deutsch |")
    readme.append("|-----|---------|---------|")
    for key, en_val, de_val in missing_added:
        en_escaped = en_val.replace('|', '\\|')
        de_escaped = de_val.replace('|', '\\|')
        readme.append(f"| `{key}` | {en_escaped} | {de_escaped} |")
    readme.append("")

readme_path = os.path.join(BASE_DIR, 'docs/i18n-german-translations.md')
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(readme))

print(f"✅ {len(changed_keys)} Keys übersetzt")
if chinese_fixed:
    print(f"✅ {len(chinese_fixed)} chinesische Textreste korrigiert")
if remaining_chinese:
    print(f"⚠️  {len(remaining_chinese)} verbleibende chinesische Textreste")
if already_translated:
    print(f"ℹ️  {len(already_translated)} Keys bereits übersetzt (übersprungen)")
print(f"\n📄 README: docs/i18n-german-translations.md")
print(f"📝 de.json aktualisiert")
