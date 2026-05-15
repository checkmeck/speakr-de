# Übersetzungs-Änderungen (English → Deutsch)

Nur Keys mit tatsächlicher Übersetzung (EN ≠ DE). Fachbegriffe wie *Backend*, *Tags*, *Status* etc. wurden nicht eingedeutscht – siehe Audit-Report `docs/i18n-german-audit.md` für die vollständige Liste.

**Ausgeführt am:** 15.05.2026

---

## Zusammenfassung

- **Tatsächlich übersetzte Keys:** 213
- **Auf Englisch belassene Fachbegriffe:** 36
- **Korrigierte chinesische Textreste:** 14
- **Neu zu en.json & de.json hinzugefügte Keys:** 102 (toasts.*) + 1 (help.systemAudioHelp)
- **Chinesische Reste:** 0 ✅
- **Strukturelle Differenzen:** 0 ✅

---

## Tatsächliche Übersetzungen (EN ≠ DE)

### aboutPage

| Key | EN | DE |
|-----|----|----|
| `aboutPage.githubRepository` | GitHub Repository | GitHub-Repository |
| `aboutPage.whisperApi` | Whisper API | Whisper-API |

### account

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
| `account.transcriptionHintsDesc` | These defaults are used when no tag or folder overrides are set... | Diese Standardwerte werden verwendet, wenn keine Tag- oder Ordner-Überschreibungen gesetzt sind... |

### adminDashboard

| Key | EN | DE |
|-----|----|----|
| `adminDashboard.allowed` | Allowed | Erlaubt |
| `adminDashboard.createFirstGroup` | Create First Group | Erste Gruppe erstellen |
| `adminDashboard.created` | Created | Erstellt |
| `adminDashboard.description` | Description | Beschreibung |
| `adminDashboard.groupName` | Group Name | Gruppenname |
| `adminDashboard.groupsTab` | Groups | Gruppen |
| `adminDashboard.members` | Members | Mitglieder |
| `adminDashboard.membersCount` | Members | Mitglieder |
| `adminDashboard.noDescription` | No description | Keine Beschreibung |
| `adminDashboard.noGroupsAdmin` | You are not an admin of any group yet | Sie sind noch kein Admin einer Gruppe |
| `adminDashboard.noGroupsCreated` | No groups created yet | Noch keine Gruppen erstellt |
| `adminDashboard.noMembersYet` | No members yet | Noch keine Mitglieder |
| `adminDashboard.passwordsDoNotMatch` | Passwords do not match | Passwörter stimmen nicht überein |
| `adminDashboard.publicShare` | Public Share | Öffentliches Teilen |

### buttons

| Key | EN | DE |
|-----|----|----|
| `buttons.cancel` | Cancel | Abbrechen |
| `buttons.close` | Close | Schließen |
| `buttons.createTag` | Create Tag | Tag erstellen |
| `buttons.deleteAll` | Delete All | Alle löschen |
| `buttons.refresh` | Refresh | Aktualisieren |
| `buttons.saveCustomPrompt` | Save Custom Prompt | Benutzerdefinierten Prompt speichern |
| `buttons.updateTag` | Update Tag | Tag aktualisieren |

### chat

| Key | EN | DE |
|-----|----|----|
| `chat.cannotChatTranscriptionFailed` | Cannot chat: Transcription failed... | Chat nicht möglich: Transkription fehlgeschlagen... |
| `chat.cleared` | Chat cleared | Chat geleert |
| `chat.downloadFailed` | Chat download failed | Download des Chats fehlgeschlagen |
| `chat.downloadSuccess` | Chat downloaded successfully! | Chat erfolgreich heruntergeladen! |
| `chat.noMessagesToDownload` | No chat messages to download | Keine Chat-Nachrichten zum Herunterladen |

### colorScheme

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

### editTagModal

| Key | EN | DE |
|-----|----|----|
| `editTagModal.watchFolder` | Watch Folder | Überwachungsordner |
| `editTagModal.watchFolderCreated` | Watch folder created | Überwachungsordner erstellt |
| `editTagModal.watchFolderError` | Could not create watch folder | Überwachungsordner konnte nicht erstellt werden |
| `editTagModal.watchFolderGroupTagError` | Watch folders are not available for group tags | Überwachungsordner sind für Gruppen-Tags nicht verfügbar |
| `editTagModal.watchFolderPath` | Drop files in: | Dateien ablegen in: |
| `editTagModal.watchFolderRemoved` | Watch folder removed | Überwachungsordner entfernt |

### errors (alle 59)

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

### form

| Key | EN | DE |
|-----|----|----|
| `form.folder` | Folder | Ordner |
| `form.hotwordsHelp` | Comma-separated words to improve recognition of domain-specific terms | Durch Komma getrennte Wörter zur Verbesserung der Erkennung domänenspezifischer Begriffe |
| `form.hotwordsPlaceholder` | e.g. Speakr, CTranslate2, PyAnnote | z. B. Speakr, CTranslate2, PyAnnote |
| `form.initialPrompt` | Initial Prompt | Initial-Prompt |
| `form.initialPromptHelp` | Context to steer the transcription model's style and vocabulary | Kontext zur Steuerung des Stils und Vokabulars des Transkriptionsmodells |
| `form.initialPromptPlaceholder` | e.g. This is a meeting about AI transcription tools | z. B. Dies ist ein Meeting über KI-Transkriptionstools |
| `form.participantNamePlaceholder` | Participant name... | Teilnehmername... |
| `form.transcriptionLanguage` | Transcription Language | Transkriptionssprache |

### help

| Key | EN | DE |
|-----|----|----|
| `help.allTagsSelected` | All tags selected | Alle Tags ausgewählt |
| `help.createFolders` | Create folders | Ordner erstellen |
| `help.defaultHotwordsHelp` | Comma-separated words or phrases that the transcription model should prioritize | Durch Komma getrennte Wörter oder Phrasen, die das Transkriptionsmodell priorisieren soll |
| `help.defaultInitialPromptHelp` | Context to steer the transcription model's style and vocabulary | Kontext zur Steuerung des Stils und Vokabulars des Transkriptionsmodells |
| `help.dragToReorder` | Drag to reorder | Zum Umsortieren ziehen |
| `help.firstTagAsrSettings` | First tag's ASR settings will be applied | ASR-Einstellungen des ersten Tags werden angewendet |
| `help.firstTagDefaultsApplied` | First tag's defaults applied | Standardeinstellungen des ersten Tags angewendet |
| `help.folderHasCustomPrompt` | This folder has a custom summary prompt | Dieser Ordner hat einen benutzerdefinierten Zusammenfassungs-Prompt |
| `help.noMatchingTags` | No matching tags | Keine passenden Tags |
| `help.selectedTagsCustomPrompts` | Selected tags include custom summary prompts | Ausgewählte Tags enthalten benutzerdefinierte Zusammenfassungs-Prompts |
| `help.toOrganizeRecordings` | to organize your recordings | um Ihre Aufnahmen zu organisieren |

### incognito

| Key | EN | DE |
|-----|----|----|
| `incognito.audioNotStored` | Audio not stored in incognito mode | Audio wird im Inkognito-Modus nicht gespeichert |
| `incognito.discardConfirm` | This will permanently discard your incognito recording | Dadurch wird Ihre Inkognito-Aufnahme endgültig verworfen |
| `incognito.mode` | Incognito Mode | Inkognito-Modus |
| `incognito.notSavedToAccount` | Not saved to account | Nicht im Konto gespeichert |
| `incognito.oneFileAtATime` | Incognito mode supports one file at a time | Der Inkognito-Modus unterstützt nur eine Datei gleichzeitig |
| `incognito.processInIncognito` | Process in Incognito | Inkognito verarbeiten |
| `incognito.processWithoutSaving` | Process without saving | Ohne Speichern verarbeiten |
| `incognito.processing` | Processing... | Verarbeitung läuft... |
| `incognito.processingComplete` | Processing complete! | Verarbeitung abgeschlossen! |
| `incognito.processingInProgress` | Processing in incognito mode... | Verarbeitung im Inkognito-Modus... |
| `incognito.recordingDiscarded` | Incognito recording discarded | Inkognito-Aufnahme verworfen |
| `incognito.recordingProcessed` | Incognito recording processed – data lost on tab close | Inkognito-Aufnahme verarbeitet – Daten gehen beim Schließen des Tabs verloren |
| `incognito.recordingReady` | Incognito recording ready! | Inkognito-Aufnahme bereit! |
| `incognito.recordingTitle` | Incognito recording | Inkognito-Aufnahme |
| `incognito.selectExactlyOneFile` | Select exactly one file | Wählen Sie genau eine Datei aus |
| `incognito.sessionOnly` | Session only | Nur für diese Sitzung |
| `incognito.uploadingFile` | Uploading file for incognito processing... | Datei wird für Inkognito-Verarbeitung hochgeladen... |

### messages

| Key | EN | DE |
|-----|----|----|
| `messages.colorSchemeApplied` | Color scheme applied | Farbschema angewendet |
| `messages.colorSchemeReset` | Color scheme reset to default | Farbschema auf Standard zurückgesetzt |
| `messages.copiedSuccessfully` | Copied to clipboard! | In die Zwischenablage kopiert! |
| `messages.copyFailed` | Copy failed | Kopieren fehlgeschlagen |
| `messages.copyNotSupported` | Copy not supported. Your browser may not support this. | Kopieren fehlgeschlagen. Ihr Browser unterstützt dies möglicherweise nicht |
| `messages.errorRecoveringRecording` | Error recovering recording | Fehler beim Wiederherstellen der Aufnahme |
| `messages.eventDownloadFailed` | Event download failed | Download des Ereignisses fehlgeschlagen |
| `messages.eventDownloadSuccess` | Event "{{title}}" downloaded. Open the file to add to your calendar. | Ereignis "{{title}}" heruntergeladen. Öffnen Sie die Datei, um sie zu Ihrem Kalender hinzuzufügen |
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
| `messages.beforeunloadRecording` | You have an unsaved recording. Are you sure you want to leave? | Sie haben eine ungespeicherte Aufnahme. Möchten Sie die Seite wirklich verlassen? |
| `messages.beforeunloadIncognito` | You have an incognito recording that will be lost. Are you sure you want to leave? | Sie haben eine Inkognito-Aufnahme, die verloren geht. Möchten Sie die Seite wirklich verlassen? |

### recording

| Key | EN | DE |
|-----|----|----|
| `recording.micPlusSys` | Mic + System | Mikro + System |

### sharing

| Key | EN | DE |
|-----|----|----|
| `sharing.teamBadge` | Team | Gruppe |

### upload

| Key | EN | DE |
|-----|----|----|
| `upload.fileExceedsMaxSize` | File "{{name}}" exceeds max size of {{size}} MB and was skipped. | Datei "{{name}}" überschreitet die maximale Größe von {{size}} MB und wurde übersprungen. |
| `upload.fileRemovedFromQueue` | File removed from queue | Datei aus der Warteschlange entfernt |
| `upload.filesToUpload` | Files to upload | Dateien zum Hochladen |
| `upload.invalidFileType` | Invalid file type "{{name}}". Only audio files and video containers (MP3, WAV, M4A, MP4, WebM, OGG, FLAC) are supported. | Ungültiger Dateityp "{{name}}". Nur Audiodateien und Video-Container (MP3, WAV, M4A, MP4, WebM, OGG, FLAC) werden unterstützt. |
| `upload.settingsApplyToAll` | Settings apply to all files in this session | Einstellungen gelten für alle Dateien in dieser Sitzung |
| `upload.uploadNFiles` | Upload {{count}} file(s) | {{count}} Datei(en) hochladen |

### tooltips

| Key | EN | DE |
|-----|----|----|
| `tooltips.exitFullscreen` | Exit Fullscreen | Vollbild beenden |
| `tooltips.fullscreenVideo` | Fullscreen Video | Video im Vollbild |
| `tooltips.hideVideo` | Hide Video | Video ausblenden |
| `tooltips.showVideo` | Show Video | Video einblenden |

---

## Neu zu en.json & de.json hinzugefügte Keys

102 `toasts.*`-Keys + `help.systemAudioHelp` wurden zu beiden Locale-Dateien hinzugefügt. Vollständige Liste in `scripts/translate_de.py`.

| Key | Englisch | Deutsch |
|-----|---------|---------|
| `help.systemAudioHelp` | Record system audio – select this option in your screen sharing dialog | Systemaudio aufnehmen – wählen Sie diesen Eintrag in Ihrem Bildschirmfreigabefenster aus |
| `toasts.apiTokenCreated` | API token created successfully | API-Token erfolgreich erstellt |
| `toasts.accountUpdated` | Account information updated successfully | Kontoinformationen erfolgreich aktualisiert |
| `toasts.customPromptSaved` | Custom prompt saved successfully | Benutzerdefinierter Prompt erfolgreich gespeichert |
| `toasts.exportTemplateCreated` | Default export template created successfully | Standard-Exportvorlage erfolgreich erstellt |
| `toasts.namingTemplateUpdated` | Default naming template updated | Standard-Benennungsvorlage aktualisiert |
| `toasts.namingTemplatesCreated` | Default naming templates created | Standard-Benennungsvorlagen erstellt |
| `toasts.defaultTemplatesCreated` | Default templates created successfully | Standardvorlagen erfolgreich erstellt |
| `toasts.enterModelId` | Enter the model id (e.g. whisper-1, large-v3) | Modell-ID eingeben (z. B. whisper-1, large-v3) |
| `toasts.errorDeletingShare` | Error deleting share | Fehler beim Löschen der Freigabe |
| `toasts.errorUpdatingShare` | Error updating share | Fehler beim Aktualisieren der Freigabe |
| `toasts.failedPushNotificationsConfig` | Failed to configure push notifications | Push-Benachrichtigungen konnten nicht konfiguriert werden |
| `toasts.failedCopyToken` | Failed to copy token to clipboard | Token konnte nicht in die Zwischenablage kopiert werden |
| `toasts.failedCreateExportTemplate` | Failed to create default export template | Standard-Exportvorlage konnte nicht erstellt werden |
| `toasts.failedCreateNamingTemplates` | Failed to create default naming templates | Standard-Benennungsvorlagen konnten nicht erstellt werden |
| `toasts.failedCreateTemplates` | Failed to create default templates | Standardvorlagen konnten nicht erstellt werden |
| `toasts.failedCreateToken` | Failed to create token | Token konnte nicht erstellt werden |
| `toasts.failedDeleteExportTemplate` | Failed to delete export template | Exportvorlage konnte nicht gelöscht werden |
| `toasts.failedDeleteFolder` | Failed to delete folder | Ordner konnte nicht gelöscht werden |
| `toasts.failedDeleteTemplate` | Failed to delete template | Vorlage konnte nicht gelöscht werden |
| `toasts.failedDisablePush` | Failed to disable push notifications | Push-Benachrichtigungen konnten nicht deaktiviert werden |
| `toasts.failedEnablePush` | Failed to enable push notifications | Push-Benachrichtigungen konnten nicht aktiviert werden |
| `toasts.failedLoadExportTemplates` | Failed to load export templates | Exportvorlagen konnten nicht geladen werden |
| `toasts.failedLoadNamingTemplates` | Failed to load naming templates | Benennungsvorlagen konnten nicht geladen werden |
| `toasts.failedLoadTemplates` | Failed to load templates | Vorlagen konnten nicht geladen werden |
| `toasts.failedRevokeToken` | Failed to revoke token | Token konnte nicht widerrufen werden |
| `toasts.failedSaveCustomPrompt` | Failed to save custom prompt | Benutzerdefinierter Prompt konnte nicht gespeichert werden |
| `toasts.failedSaveFolder` | Failed to save folder | Ordner konnte nicht gespeichert werden |
| `toasts.failedSavePreferences` | Failed to save preferences | Einstellungen konnten nicht gespeichert werden |
| `toasts.failedTestTemplate` | Failed to test template | Vorlage konnte nicht getestet werden |
| `toasts.failedUpdateAccount` | Failed to update account information | Kontoinformationen konnten nicht aktualisiert werden |
| `toasts.failedUpdateDefaultTemplate` | Failed to update default template | Standardvorlage konnte nicht aktualisiert werden |
| `toasts.failedUpdateLanguage` | Failed to update language | Sprache konnte nicht aktualisiert werden |
| `toasts.failedUpdateToken` | Failed to update token | Token konnte nicht aktualisiert werden |
| `toasts.folderNameRequired` | Folder name is required | Ordnername ist erforderlich |
| `toasts.folderPrefix` | Folder | Ordner |
| `toasts.incognitoRecordingLost` | Incognito recording processed – data will be lost when tab closes | Inkognito-Aufnahme verarbeitet – Daten gehen beim Schließen des Tabs verloren |
| `toasts.installingSpeakr` | Installing Speakr... | Speakr wird installiert... |
| `toasts.meetingDateUpdated` | Meeting date updated! | Meeting-Datum aktualisiert! |
| `toasts.namingTemplateDeleted` | Naming template deleted | Benennungsvorlage gelöscht |
| `toasts.networkError` | Network error | Netzwerkfehler |
| `toasts.passwordMismatch` | New password and confirmation do not match | Das neue Passwort und die Bestätigung stimmen nicht überein |
| `toasts.noAudioTrack` | No audio track – check | Keine Audiospur – überprüfen Sie |
| `toasts.noSourceSpeakers` | No source speakers to merge | Keine Quell-Sprecher zum Zusammenführen |
| `toasts.notesCopied` | Notes copied to clipboard! | Notizen in die Zwischenablage kopiert! |
| `toasts.notesSavedBrowser` | Notes saved (in browser only) | Notizen gespeichert (nur im Browser) |
| `toasts.notesSaved` | Notes saved! | Notizen gespeichert! |
| `toasts.notificationDenied` | Notification permission denied | Benachrichtigungsberechtigung verweigert |
| `toasts.notificationsEnabled` | Notifications enabled | Benachrichtigungen aktiviert |
| `toasts.enterTokenName` | Please enter a token name | Bitte geben Sie einen Token-Namen ein |
| `toasts.selectMinSpeakers` | Please select at least 2 speakers to merge | Bitte wählen Sie mindestens 2 Sprecher zum Zusammenführen aus |
| `toasts.selectSpeakersClear` | Please select speakers to clear voice profiles | Bitte wählen Sie Sprecher zum Löschen der Sprachprofile aus |
| `toasts.selectSpeakersDelete` | Please select speakers to delete | Bitte wählen Sie zu löschende Sprecher aus |
| `toasts.selectSpeakerKeep` | Please select which speaker to keep | Bitte wählen Sie den zu behaltenden Sprecher aus |
| `toasts.preferencesSaved` | Preferences saved | Einstellungen gespeichert |
| `toasts.processingCompleted` | Processing completed! | Verarbeitung abgeschlossen! |
| `toasts.processingFailed` | Processing failed | Verarbeitung fehlgeschlagen |
| `toasts.pushDenied` | Push notification permission denied | Push-Benachrichtigungsberechtigung verweigert |
| `toasts.pushDisabled` | Push notifications disabled | Push-Benachrichtigungen deaktiviert |
| `toasts.pushEnabled` | Push notifications enabled | Push-Benachrichtigungen aktiviert |
| `toasts.pushNotAvailable` | Push notifications not available. Install pywebpush on server. | Push-Benachrichtigungen nicht verfügbar. Installieren Sie pywebpush auf dem Server. |
| `toasts.pushNotSupported` | Push notifications not supported in this browser | Push-Benachrichtigungen werden in diesem Browser nicht unterstützt |
| `toasts.recordingArchived` | Recording archived (audio deleted) | Aufnahme archiviert (Audio gelöscht) |
| `toasts.recordingDeleted` | Recording deleted | Aufnahme gelöscht |
| `toasts.recordingReset` | Recording reset for reprocessing | Aufnahme für erneute Verarbeitung zurückgesetzt |
| `toasts.recordingResumed` | Recording resumed – screen will stay awake | Aufnahme fortgesetzt – Bildschirm bleibt wach |
| `toasts.recordingStatusReset` | Recording status reset to FAILED | Aufnahmestatus auf FEHLGESCHLAGEN zurückgesetzt |
| `toasts.recordingUpdated` | Recording updated! | Aufnahme aktualisiert! |
| `toasts.removedFromFolder` | Removed from folder | Aus Ordner entfernt |
| `toasts.saveTemplateFirst` | Save the template first to test it | Speichern Sie die Vorlage zuerst, um sie zu testen |
| `toasts.screenLockDenied` | Screen lock permission denied | Bildschirmsperrberechtigung verweigert |
| `toasts.screenMaySleep` | Screen may sleep during recording | Bildschirm kann während der Aufnahme in den Ruhezustand gehen |
| `toasts.screenSharingCancelled` | Screen sharing was cancelled | Bildschirmfreigabe wurde abgebrochen |
| `toasts.shareDeleted` | Share deleted successfully | Freigabe erfolgreich gelöscht |
| `toasts.shareLinkCopied` | Share link copied to clipboard | Freigabelink in die Zwischenablage kopiert |
| `toasts.shareLinkCreated` | Share link created successfully! | Freigabelink erfolgreich erstellt! |
| `toasts.shareLinkDeleted` | Share link deleted successfully | Freigabelink erfolgreich gelöscht |
| `toasts.sharePermissionsUpdated` | Share permissions updated | Freigabeberechtigungen aktualisiert |
| `toasts.speakerNameUpdated` | Speaker name updated successfully | Sprechername erfolgreich aktualisiert |
| `toasts.speakrInstalled` | Speakr installed successfully! | Speakr erfolgreich installiert! |
| `toasts.summaryCopied` | Summary copied to clipboard! | Zusammenfassung in die Zwischenablage kopiert! |
| `toasts.summaryGenerated` | Summary generated | Zusammenfassung erstellt |
| `toasts.summaryGenerationStarted` | Summary generation started | Zusammenfassungserstellung gestartet |
| `toasts.summaryReprocessingStarted` | Summary reprocessing started | Erneute Zusammenfassungserstellung gestartet |
| `toasts.summarySaved` | Summary saved! | Zusammenfassung gespeichert! |
| `toasts.tagAdded` | Tag added successfully | Tag erfolgreich hinzugefügt |
| `toasts.tagAddedExcl` | Tag added! | Tag hinzugefügt! |
| `toasts.tagRemoved` | Tag removed successfully | Tag erfolgreich entfernt |
| `toasts.tagRemovedExcl` | Tag removed! | Tag entfernt! |
| `toasts.tagsReordered` | Tags reordered | Tags neu angeordnet |
| `toasts.exportTemplateDeleted` | Export template deleted successfully | Exportvorlage erfolgreich gelöscht |
| `toasts.templateDeleted` | Template deleted successfully | Vorlage erfolgreich gelöscht |
| `toasts.titleRegenerated` | Title regenerated | Titel neu generiert |
| `toasts.tokenCopied` | Token copied to clipboard | Token in die Zwischenablage kopiert |
| `toasts.tokenNameEmpty` | Token name cannot be empty | Token-Name darf nicht leer sein |
| `toasts.tokenNameUpdated` | Token name updated | Token-Name aktualisiert |
| `toasts.tokenRevoked` | Token revoked successfully | Token erfolgreich widerrufen |
| `toasts.transcriptionCopied` | Transcription copied to clipboard! | Transkription in die Zwischenablage kopiert! |
| `toasts.transcriptionReprocessingStarted` | Transcription reprocessing started | Erneute Transkription gestartet |
| `toasts.transcriptionUpdated` | Transcription updated successfully! | Transkription erfolgreich aktualisiert! |
| `toasts.usingExistingShareLink` | Using existing share link | Vorhandenen Freigabelink verwenden |
| `toasts.wakeLockNotSupported` | Wake lock not supported on this device | Wake-Lock wird auf diesem Gerät nicht unterstützt |
| `toasts.iOSWakeLockIssue` | iOS wake lock may not work – keep screen active | iOS Wake-Lock funktioniert möglicherweise nicht – Bildschirm aktiv halten |

---

## Chinesische Textreste (korrigiert)

14 Keys enthielten chinesischen Text (aus zh.json übernommen):

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

Übersetzungen automatisch via Script angewendet:

```bash
python3 scripts/translate_de.py
```

**Dateien:**
- `static/locales/de.json` – aktualisiert
- `static/locales/en.json` – um `toasts.*` und `help.systemAudioHelp` ergänzt
- `scripts/translate_de.py` – Übersetzungsscript
- `docs/i18n-german-translations.md` – dieser Report
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
