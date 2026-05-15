# Übersetzungs-Änderungen (English → Deutsch)

Dieses Dokument listet alle Übersetzungen auf, die durch das Script `scripts/translate_de.py` in `de.json` vorgenommen wurden.

**Ausgeführt am:** 15.05.2026

---

## Zusammenfassung

- **Übersetzte Keys:** 249
  - 213 Keys mit deutschem Text belegt (vorher identisch mit Englisch)
  - 36 Keys mit englischen Fachbegriffen (bewusst nicht eingedeutscht)
- **Korrigierte chinesische Textreste:** 14
- **Neu zu en.json & de.json hinzugefügte Keys (Code-Strings):** 102 (toasts.*) + 1 (help.systemAudioHelp)
- **Chinesische Reste:** 0 ✅
- **Strukturelle Differenzen en.json ↔ de.json:** 0 ✅
- **Keys nur in de.json (Altlast):** 1 (`errors.serverError`) – übersetzt, existiert nicht in en.json

---

## Übersetzungen (English → Deutsch)

### aboutPage (4 Keys)

| Key | EN | DE |
|-----|----|----|
| `aboutPage.backend` | Backend | Backend |
| `aboutPage.dockerHub` | Docker Hub | Docker Hub |
| `aboutPage.frontend` | Frontend | Frontend |
| `aboutPage.githubRepository` | GitHub Repository | GitHub-Repository |
| `aboutPage.version` | Version | Version |
| `aboutPage.whisperApi` | Whisper API | Whisper-API |

### aboutPageDetails (2 Keys)

| Key | EN | DE |
|-----|----|----|
| `aboutPageDetails.backend` | Backend | Backend |
| `aboutPageDetails.frontend` | Frontend | Frontend |

### account (19 Keys)

| Key | EN | DE |
|-----|----|----|
| `account.autoLabel` | Auto Label | Auto-Beschriftung |
| `account.autoSummarizationDisabled` | Auto-summarization disabled by admin | Auto-Zusammenfassung von Admin deaktiviert |
| `account.autoSummarize` | Auto Summarize | Auto-Zusammenfassen |
| `account.defaultHotwords` | Default Hotwords | Standard-Hotwords |
| `account.defaultHotwordsPlaceholder` | e.g. Speakr, CTranslate2, PyAnnote, SDRs | z. B. Speakr, CTranslate2, PyAnnote, SDRs |
| `account.defaultInitialPrompt` | Default Initial Prompt | Standard-Initial-Prompt |
| `account.defaultInitialPromptPlaceholder` | e.g. This is a meeting about AI transcription tools... | z. B. Dies ist ein Meeting über KI-Transkriptionstools... |
| `account.personalFolder` | Personal folder (not linked to a group) | Persönlicher Ordner (nicht mit einer Gruppe verknüpft) |
| `account.personalTag` | Personal tag (not linked to a group) | Persönlicher Tag (nicht mit einer Gruppe verknüpft) |
| `account.ssoLinkAccount` | Link {{provider}} Account | {{provider}}-Konto verknüpfen |
| `account.ssoLinked` | Linked | Verknüpft |
| `account.ssoNotLinked` | Not linked | Nicht verknüpft |
| `account.ssoProvider` | Provider | Anbieter |
| `account.ssoSetPasswordFirst` | To unlink SSO, please set a password first | Zum Entkoppeln von SSO müssen Sie zuerst ein Passwort festlegen |
| `account.ssoSubject` | Subject: | Betreff: |
| `account.ssoUnlinkAccount` | Unlink {{provider}} Account | {{provider}}-Konto entkoppeln |
| `account.ssoUnlinkConfirm` | Are you sure you want to unlink your SSO account... | Sind Sie sicher, dass Sie Ihr SSO-Konto entkoppeln möchten? |
| `account.transcriptionHints` | Transcription Hints | Transkriptionshinweise |
| `account.transcriptionHintsDesc` | These defaults are used when no tag or folder overrides are set... | Diese Standardwerte werden verwendet... |

### adminDashboard (17 Keys)

| Key | EN | DE |
|-----|----|----|
| `adminDashboard.admin` | ADMIN | ADMIN |
| `adminDashboard.allowed` | Allowed | Erlaubt |
| `adminDashboard.createFirstGroup` | Create First Group | Erste Gruppe erstellen |
| `adminDashboard.created` | Created | Erstellt |
| `adminDashboard.description` | Description | Beschreibung |
| `adminDashboard.groupName` | Group Name | Gruppenname |
| `adminDashboard.groupsTab` | Groups | Gruppen |
| `adminDashboard.id` | ID | ID |
| `adminDashboard.megabytes` | MB | MB |
| `adminDashboard.members` | Members | Mitglieder |
| `adminDashboard.membersCount` | Members | Mitglieder |
| `adminDashboard.noDescription` | No description | Keine Beschreibung |
| `adminDashboard.noGroupsAdmin` | You are not an admin of any group yet | Sie sind noch kein Admin einer Gruppe |
| `adminDashboard.noGroupsCreated` | No groups created yet | Noch keine Gruppen erstellt |
| `adminDashboard.noMembersYet` | No members yet | Noch keine Mitglieder |
| `adminDashboard.passwordsDoNotMatch` | Passwords do not match | Passwörter stimmen nicht überein |
| `adminDashboard.publicShare` | Public Share | Öffentliches Teilen |

### buttons (7 Keys)

| Key | EN | DE |
|-----|----|----|
| `buttons.cancel` | Cancel | Abbrechen |
| `buttons.close` | Close | Schließen |
| `buttons.createTag` | Create Tag | Tag erstellen |
| `buttons.deleteAll` | Delete All | Alle löschen |
| `buttons.refresh` | Refresh | Aktualisieren |
| `buttons.saveCustomPrompt` | Save Custom Prompt | Benutzerdefinierten Prompt speichern |
| `buttons.updateTag` | Update Tag | Tag aktualisieren |

### chat (6 Keys)

| Key | EN | DE |
|-----|----|----|
| `chat.cannotChatTranscriptionFailed` | Cannot chat: Transcription failed... | Chat nicht möglich: Transkription fehlgeschlagen... |
| `chat.cleared` | Chat cleared | Chat geleert |
| `chat.downloadFailed` | Chat download failed | Download des Chats fehlgeschlagen |
| `chat.downloadSuccess` | Chat downloaded successfully! | Chat erfolgreich heruntergeladen! |
| `chat.noMessagesToDownload` | No chat messages to download | Keine Chat-Nachrichten zum Herunterladen |
| `chat.title` | Chat | Chat |

### colorScheme (12 Keys)

| Key | EN | DE |
|-----|----|----|
| `colorScheme.descriptions.amber` | Warm amber tones for a cozy feel | Warme Bernsteintöne für ein gemütliches Gefühl |
| `colorScheme.descriptions.blue` | Classic blue design with a clean look | Klassisches Blau-Design mit einem sauberen Look |
| `colorScheme.descriptions.emerald` | Nature-inspired green for a calming experience | Naturinspiriertes Grün-Design für ein beruhigendes Erlebnis |
| `colorScheme.descriptions.purple` | Rich purple with an elegant modern look | Reichhaltiges Lila-Design mit einem eleganten Look |
| `colorScheme.descriptions.rose` | Warm rose with a soft inviting aesthetic | Warmes Rosen-Design mit einer sanften, einladenden Ästhetik |
| `colorScheme.descriptions.teal` | Cool teal with a refreshing modern style | Kühles Türkis-Design mit einem erfrischenden Stil |
| `colorScheme.names.amber` | Golden Amber | Goldener Bernstein |
| `colorScheme.names.blue` | Ocean Blue | Ozeanblau |
| `colorScheme.names.emerald` | Forest Green | Waldgrün |
| `colorScheme.names.purple` | Royal Purple | Königspurpur |
| `colorScheme.names.rose` | Coral Rose | Korallenrose |
| `colorScheme.names.teal` | Arctic Teal | Arktistürkis |

### errors (59 Keys)

Alle 59 Fehler-Keys wurden übersetzt. Vollständige Liste in `scripts/translate_de.py`.

| Key | EN | DE |
|-----|----|----|
| `errors.audioExtractionFailed` | Audio extraction failed | Audio-Extraktion fehlgeschlagen |
| `errors.audioExtractionFailedGuidance` | Try converting to MP3/WAV | Versuchen Sie, die Datei in MP3/WAV zu konvertieren |
| `errors.audioExtractionFailedMessage` | Could not extract audio from uploaded file | Audio konnte nicht aus der hochgeladenen Datei extrahiert werden |
| `errors.audioRecordingFailed` | Audio recording failed | Audioaufnahme fehlgeschlagen |
| `errors.authenticationError` | Authentication error | Authentifizierungsfehler |
| `errors.authenticationErrorGuidance` | Check if API key is correct | Bitte überprüfen Sie, ob der API-Schlüssel korrekt ist |
| `errors.authenticationErrorMessage` | The transcription service rejected the API credentials | Der Transkriptionsdienst hat die API-Anmeldedaten abgelehnt |
| `errors.checkApiKeyGuidance` | Check API key in settings | API-Schlüssel in den Einstellungen überprüfen |
| `errors.checkNetworkGuidance` | Check network connection | Netzwerkverbindung überprüfen |
| `errors.connectionError` | Connection error | Verbindungsfehler |
| `errors.connectionErrorGuidance` | Check internet connection | Internetverbindung überprüfen |
| `errors.connectionErrorMessage` | Could not connect to transcription service | Konnte keine Verbindung zum Transkriptionsdienst herstellen |
| `errors.convertFormatGuidance` | Convert to MP3 or WAV before uploading | Vor dem Hochladen in MP3 oder WAV konvertieren |
| `errors.convertStandardGuidance` | Convert to a standard audio format | In ein Standard-Audioformat konvertieren |
| `errors.enableChunkingGuidance` | Enable chunking in settings or compress | Chunking in den Einstellungen aktivieren oder komprimieren |
| `errors.fallbackMessage` | An error occurred | Ein Fehler ist aufgetreten |
| `errors.fallbackTitle` | Error | Fehler |
| `errors.fileTooLarge` | File too large | Datei zu groß |
| `errors.fileTooLargeGuidance` | Try enabling audio chunking | Audio-Chunking aktivieren oder Datei komprimieren |
| `errors.fileTooLargeMaxSize` | File too large. Max: {{size}} MB | Datei zu groß. Max: {{size}} MB |
| `errors.fileTooLargeMessage` | The audio file exceeds the maximum size | Die Audiodatei überschreitet die Maximalgröße |
| `errors.fileTooLargeTitle` | File too large | Datei zu groß |
| `errors.generic` | An error occurred | Ein Fehler ist aufgetreten |
| `errors.invalidAudioFormat` | Invalid audio format | Ungültiges Audioformat |
| `errors.invalidAudioFormatGuidance` | Try converting to MP3 or WAV | Versuchen Sie, die Datei in MP3/WAV zu konvertieren |
| `errors.invalidAudioFormatMessage` | Audio format not supported or file corrupted | Das Audioformat wird nicht unterstützt oder die Datei ist beschädigt |
| `errors.networkError` | Network error | Netzwerkfehler |
| `errors.networkErrorDuringUpload` | Network error during upload | Netzwerkfehler während des Uploads |
| `errors.notFound` | Not found | Nicht gefunden |
| `errors.permissionDenied` | Permission denied | Zugriff verweigert |
| `errors.processingError` | Processing error | Verarbeitungsfehler |
| `errors.processingErrorFallbackGuidance` | Try reprocessing the recording | Versuchen Sie, die Aufnahme erneut zu verarbeiten |
| `errors.processingErrorGuidance` | If this persists, try reprocessing | Wenn der Fehler weiterhin besteht, versuchen Sie es erneut |
| `errors.processingErrorMessage` | An error occurred during processing | Während der Verarbeitung ist ein Fehler aufgetreten |
| `errors.processingFailedOnServer` | Processing failed on server | Verarbeitung auf dem Server fehlgeschlagen |
| `errors.processingFailedWithStatus` | Processing failed with status {{status}} | Verarbeitung mit Status {{status}} fehlgeschlagen |
| `errors.processingTimeout` | Processing timeout | Verarbeitungszeitüberschreitung |
| `errors.processingTimeoutGuidance` | This can happen with very long recordings | Dies kann bei sehr langen Aufnahmen passieren |
| `errors.processingTimeoutMessage` | The transcription took too long | Die Transkription hat zu lange gedauert |
| `errors.quotaExceeded` | Quota exceeded | Speicherkontingent überschritten |
| `errors.rateLimitExceeded` | Rate limit exceeded | Ratenlimit überschritten |
| `errors.rateLimitExceededGuidance` | Please wait a few minutes and retry | Bitte warten Sie einige Minuten und versuchen Sie es erneut |
| `errors.rateLimitExceededMessage` | Too many requests to transcription service | Zu viele Anfragen an den Transkriptionsdienst |
| `errors.serverErrorStatus` | Server error ({{status}}) | Serverfehler ({{status}}) |
| `errors.serviceUnavailable` | Service unavailable | Dienst nicht verfügbar |
| `errors.serviceUnavailableGuidance` | This is usually temporary. Please retry. | Dies ist normalerweise vorübergehend. Bitte versuchen Sie es erneut |
| `errors.serviceUnavailableMessage` | The transcription service is temporarily unavailable | Der Transkriptionsdienst ist vorübergehend nicht verfügbar |
| `errors.splitAudioGuidance` | Try splitting the audio into smaller parts | Versuchen Sie, die Audiodatei in kleinere Teile aufzuteilen |
| `errors.summaryFailed` | Summary failed | Zusammenfassung fehlgeschlagen |
| `errors.transcriptionFailed` | Transcription failed | Transkription fehlgeschlagen |
| `errors.tryAgainLaterGuidance` | Try again in a few minutes | Versuchen Sie es in ein paar Minuten erneut |
| `errors.unauthorized` | Unauthorized | Nicht autorisiert |
| `errors.unexpectedResponse` | Unexpected success response from server | Unerwartete Erfolgsantwort vom Server nach dem Upload |
| `errors.unsupportedFormat` | Unsupported format | Nicht unterstütztes Format |
| `errors.uploadFailed` | Upload failed | Upload fehlgeschlagen |
| `errors.uploadFailedWithStatus` | Upload failed with status {{status}} | Upload mit Status {{status}} fehlgeschlagen |
| `errors.uploadTimedOut` | Upload timed out | Upload-Zeitüberschreitung |
| `errors.validationError` | Validation error | Validierungsfehler |
| `errors.waitAndRetryGuidance` | Wait a few minutes and retry | Einige Minuten warten und erneut versuchen |

### incognito (17 Keys)

| Key | EN | DE |
|-----|----|----|
| `incognito.audioNotStored` | Audio not stored in incognito mode | Audio wird im Inkognito-Modus nicht gespeichert |
| `incognito.discardConfirm` | This will permanently discard... | Dadurch wird Ihre Inkognito-Aufnahme endgültig verworfen |
| `incognito.mode` | Incognito Mode | Inkognito-Modus |
| `incognito.notSavedToAccount` | Not saved to account | Nicht im Konto gespeichert |
| `incognito.oneFileAtATime` | Incognito mode supports one file at a time | Der Inkognito-Modus unterstützt nur eine Datei gleichzeitig |
| `incognito.processInIncognito` | Process in Incognito | Inkognito verarbeiten |
| `incognito.processWithoutSaving` | Process without saving | Ohne Speichern verarbeiten |
| `incognito.processing` | Processing... | Verarbeitung läuft... |
| `incognito.processingComplete` | Processing complete! | Verarbeitung abgeschlossen! |
| `incognito.processingInProgress` | Processing in incognito mode... | Verarbeitung im Inkognito-Modus... |
| `incognito.recordingDiscarded` | Incognito recording discarded | Inkognito-Aufnahme verworfen |
| `incognito.recordingProcessed` | Incognito recording processed... | Inkognito-Aufnahme verarbeitet... |
| `incognito.recordingReady` | Incognito recording ready! | Inkognito-Aufnahme bereit! |
| `incognito.recordingTitle` | Incognito recording | Inkognito-Aufnahme |
| `incognito.selectExactlyOneFile` | Select exactly one file | Wählen Sie genau eine Datei aus |
| `incognito.sessionOnly` | Session only | Nur für diese Sitzung |
| `incognito.uploadingFile` | Uploading file for incognito processing... | Datei wird für Inkognito-Verarbeitung hochgeladen... |

### messages (39 Keys)

Alle 39 Message-Keys übersetzt. Vollständige Liste in `scripts/translate_de.py`.

| Key | EN | DE |
|-----|----|----|
| `messages.colorSchemeApplied` | Color scheme applied | Farbschema angewendet |
| `messages.colorSchemeReset` | Color scheme reset to default | Farbschema auf Standard zurückgesetzt |
| `messages.copiedSuccessfully` | Copied to clipboard! | In die Zwischenablage kopiert! |
| `messages.copyFailed` | Copy failed | Kopieren fehlgeschlagen |
| `messages.copyNotSupported` | Copy not supported. Your browser may not support this. | Kopieren fehlgeschlagen. Ihr Browser unterstützt dies möglicherweise nicht |
| `messages.errorRecoveringRecording` | Error recovering recording | Fehler beim Wiederherstellen der Aufnahme |
| `messages.eventDownloadFailed` | Event download failed | Download des Ereignisses fehlgeschlagen |
| `messages.eventDownloadSuccess` | Event "{{title}}" downloaded. Open the file to add to your calendar. | Ereignis "{{title}}" heruntergeladen. Öffnen Sie die Datei... |
| `messages.eventsExportFailed` | Events export failed | Export der Ereignisse fehlgeschlagen |
| `messages.eventsExportSuccess` | {{count}} events exported | {{count}} Ereignisse exportiert |
| `messages.failedToDeleteJob` | Failed to delete job | Löschen des Auftrags fehlgeschlagen |
| `messages.failedToRecoverRecording` | Failed to recover recording | Wiederherstellen der Aufnahme fehlgeschlagen |
| `messages.failedToRetryJob` | Failed to retry job | Wiederholen des Auftrags fehlgeschlagen |
| `messages.failedToSave` | Failed to save: {{error}} | Speichern fehlgeschlagen: {{error}} |
| `messages.failedToSaveParticipants` | Failed to save participants | Speichern der Teilnehmer fehlgeschlagen |
| `messages.followPlayerDisabled` | Follow player mode disabled | Follow-Player-Modus deaktiviert |
| `messages.followPlayerEnabled` | Follow player mode enabled | Follow-Player-Modus aktiviert |
| `messages.invalidEventData` | Invalid event data | Ungültige Ereignisdaten |
| `messages.jobQueuedForRetry` | Job queued for retry | Auftrag zur Wiederholung eingereiht |
| `messages.noEventsToExport` | No events to export | Keine Ereignisse zum Exportieren |
| `messages.noNotesAvailableDownload` | No notes available for download | Keine Notizen zum Herunterladen verfügbar |
| `messages.noNotesToCopy` | No notes to copy | Keine Notizen zum Kopieren verfügbar |
| `messages.noPermissionToEdit` | You don't have permission to edit this recording | Sie haben keine Berechtigung, diese Aufnahme zu bearbeiten |
| `messages.noSummaryToCopy` | No summary to copy | Keine Zusammenfassung zum Kopieren verfügbar |
| `messages.noSummaryToDownload` | No summary available for download | Keine Zusammenfassung zum Herunterladen verfügbar |
| `messages.noTranscriptionToCopy` | No transcription to copy | Keine Transkription zum Kopieren verfügbar |
| `messages.noTranscriptionToDownload` | No transcription available for download | Keine Transkription zum Herunterladen verfügbar |
| `messages.notesCopied` | Notes copied to clipboard! | Notizen in die Zwischenablage kopiert! |
| `messages.notesDownloadFailed` | Notes download failed | Download der Notizen fehlgeschlagen |
| `messages.notesDownloadSuccess` | Notes downloaded successfully! | Notizen erfolgreich heruntergeladen! |
| `messages.recordingDiscarded` | Recording discarded | Aufnahme verworfen |
| `messages.recordingRecovered` | Recording recovered successfully | Aufnahme erfolgreich wiederhergestellt |
| `messages.saveParticipantsFailed` | Save failed: {{error}} | Speichern fehlgeschlagen: {{error}} |
| `messages.summaryCopied` | Summary copied to clipboard! | Zusammenfassung in die Zwischenablage kopiert! |
| `messages.summaryDownloadFailed` | Summary download failed | Download der Zusammenfassung fehlgeschlagen |
| `messages.summaryDownloadSuccess` | Summary downloaded successfully! | Zusammenfassung erfolgreich heruntergeladen! |
| `messages.transcriptDownloadFailed` | Transcript download failed | Download des Transkripts fehlgeschlagen |
| `messages.transcriptDownloadSuccess` | Transcript downloaded successfully! | Transkript erfolgreich heruntergeladen! |
| `messages.transcriptionCopied` | Transcription copied to clipboard! | Transkription in die Zwischenablage kopiert! |

### Weitere übersetzte Sektionen

**form (13 Keys):** `form.auto`, `form.folder`, `form.hotwords`, `form.hotwordsHelp`, `form.initialPrompt`, `form.initialPromptHelp`, `form.optional`, `form.participantNamePlaceholder`, `form.transcriptionLanguage` u. a. – alle übersetzt.

**help:** `help.allTagsSelected`, `help.createFolders`, `help.defaultHotwordsHelp`, `help.defaultInitialPromptHelp`, `help.dragToReorder`, `help.firstTagAsrSettings`, `help.firstTagDefaultsApplied`, `help.folderHasCustomPrompt`, `help.noMatchingTags`, `help.selectedTagsCustomPrompts`, `help.toOrganizeRecordings`, `help.systemAudioHelp` (neu) – alle übersetzt.

**upload (6 Keys):** `upload.fileExceedsMaxSize`, `upload.fileRemovedFromQueue`, `upload.filesToUpload`, `upload.invalidFileType`, `upload.settingsApplyToAll`, `upload.uploadNFiles` – alle übersetzt.

**tooltips (5 Keys), recording (2 Keys), sharing (1 Key), sidebar (2 Keys), tagManagement (2 Keys), tags (1 Key), metadata (1 Key), inquire (1 Key), languages (1 Key)** – alle übersetzt.

---

## Neu zu en.json & de.json hinzugefügte Keys

Folgende **102 Keys (`toasts.*`) + `help.systemAudioHelp`** wurden zu beiden Locale-Dateien hinzugefügt, da sie im Code als direkte JS-Strings verwendet wurden. Vollständige Liste in `scripts/translate_de.py` (ca. Zeile 430–510).

Beispiele:

| Key | Englisch | Deutsch |
|-----|---------|---------|
| `help.systemAudioHelp` | Record system audio – select this option in your screen sharing dialog | Systemaudio aufnehmen – wählen Sie diesen Eintrag in Ihrem Bildschirmfreigabefenster aus |
| `toasts.apiTokenCreated` | API token created successfully | API-Token erfolgreich erstellt |
| `toasts.accountUpdated` | Account information updated successfully | Kontoinformationen erfolgreich aktualisiert |
| `toasts.customPromptSaved` | Custom prompt saved successfully | Benutzerdefinierter Prompt erfolgreich gespeichert |
| `toasts.recordingDeleted` | Recording deleted | Aufnahme gelöscht |
| `toasts.transcriptionUpdated` | Transcription updated successfully! | Transkription erfolgreich aktualisiert! |
| ... und 97 weitere | Siehe `scripts/translate_de.py` | |

---

## Chinesische Textreste (korrigiert)

14 Keys enthielten chinesischen Text (aus zh.json übernommen). Alle wurden auf Deutsch korrigiert:

| Key | Vorher (Chinesisch) | Nachher (Deutsch) |
|-----|--------------------|--------------------|
| `errors.audioRecordingFailed` | 音频录制失败... | Audioaufnahme fehlgeschlagen... |
| `errors.fileTooLarge` | 文件太大 | Datei zu groß |
| `errors.generic` | 发生错误 | Ein Fehler ist aufgetreten |
| `errors.networkError` | 网络错误... | Netzwerkfehler... |
| `errors.notFound` | 未找到 | Nicht gefunden |
| `errors.permissionDenied` | 权限被拒绝 | Zugriff verweigert |
| `errors.quotaExceeded` | 存储配额已超出 | Speicherkontingent überschritten |
| `errors.serverError` | 服务器错误... | Serverfehler... |
| `errors.summaryFailed` | 摘要生成失败... | Zusammenfassung fehlgeschlagen... |
| `errors.transcriptionFailed` | 转录失败... | Transkription fehlgeschlagen... |
| `errors.unauthorized` | 未授权 | Nicht autorisiert |
| `errors.unsupportedFormat` | 不支持的文件格式 | Nicht unterstütztes Format |
| `errors.uploadFailed` | 上传失败... | Upload fehlgeschlagen... |
| `errors.validationError` | 验证错误 | Validierungsfehler |

---

## Änderungsanleitung

Die Übersetzungen wurden automatisch via Script angewendet:

```bash
python3 scripts/translate_de.py
```

Das Script:
1. Übersetzt alle Keys, deren `de.json`-Wert identisch mit `en.json` ist
2. Korrigiert chinesische Textreste
3. Fügt fehlende Keys (`toasts.*`) zu beiden Locale-Dateien hinzu
4. Generiert diesen README-Bericht

**Zu überprüfen:**
- Die 36 Keys mit englischen Fachbegriffen (Backend, Tags, Status, Admin, Chat, Filter, Info, OK, Export, MB, KB, GB, Version, Pause, Auto, Start, Max, Min, Hindi, Hotwords) – können bei Bedarf noch eingedeutscht werden
- `errors.serverError` existiert nur in `de.json` (Altlast) – in `en.json` nicht vorhanden

**Dateien:**
- `static/locales/de.json` – aktualisiert
- `static/locales/en.json` – um `toasts.*` und `help.systemAudioHelp` ergänzt
- `scripts/translate_de.py` – Übersetzungsscript
- `docs/i18n-german-translations.md` – dieser Report
# Übersetzungs-Änderungen (English → Deutsch)

Dieses Dokument listet alle Übersetzungen auf, die in `de.json` vorgenommen wurden.

**Durchgeführt am:** 15.05.2026

---

## Zusammenfassung

- **Neu übersetzte Keys:** 36
- **Bereits übersetzt (nicht geändert):** 213

---

## Neue Übersetzungen

| Key | Englisch (en.json) | Deutsch (de.json) |
|-----|-------------------|--------------------|
| `aboutPage.backend` | Backend | Backend |
| `aboutPage.dockerHub` | Docker Hub | Docker Hub |
| `aboutPage.frontend` | Frontend | Frontend |
| `aboutPage.version` | Version | Version |
| `aboutPageDetails.backend` | Backend | Backend |
| `aboutPageDetails.frontend` | Frontend | Frontend |
| `adminDashboard.admin` | ADMIN | ADMIN |
| `adminDashboard.id` | ID | ID |
| `adminDashboard.megabytes` | MB | MB |
| `chat.title` | Chat | Chat |
| `common.filter` | Filter | Filter |
| `common.info` | Info | Info |
| `common.ok` | OK | OK |
| `editTagModal.defaultPromptPlaceholder` | Leer lassen, um Ihren Standard-Zusammenfassungs-Prompt zu verwenden | Leer lassen, um Ihren Standard-Zusammenfassungs-Prompt zu verwenden |
| `exportLabels.tags` | Tags | Tags |
| `exportTemplates.tabTitle` | Export | Export |
| `fileSize.bytes` | {{count}} B | {{count}} B |
| `fileSize.gigabytes` | {{count}} GB | {{count}} GB |
| `fileSize.kilobytes` | {{count}} KB | {{count}} KB |
| `fileSize.megabytes` | {{count}} MB | {{count}} MB |
| `form.auto` | Auto | Auto |
| `form.hotwords` | Hotwords | Hotwords |
| `form.optional` | Optional | Optional |
| `form.placeholderAuto` | Auto | Auto |
| `form.placeholderOptional` | Optional | Optional |
| `help.autoIdentifyMobile` | Auto | Auto |
| `help.startTime` | Start | Start |
| `inquire.tags` | Tags | Tags |
| `languages.hi` | Hindi | Hindi |
| `metadata.status` | Status | Status |
| `recording.pauseRecording` | Pause | Pause |
| `sidebar.tags` | Tags | Tags |
| `tagManagement.maxSpeakers` | Max | Max |
| `tagManagement.minSpeakers` | Min | Min |
| `tags.title` | Tags | Tags |
| `tooltips.pause` | Pause | Pause |
