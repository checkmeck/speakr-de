# German Translations — Implementation List

Add these entries to `de.json`. Use the i18n key format as shown.

---

## aboutPage

| Key | English | German |
|------|---------|--------|
| aboutPage.githubRepository | GitHub Repository | GitHub-Repository |
| aboutPage.whisperApi | Whisper API | Whisper-API |

## account

| Key | English | German |
|------|---------|--------|
| account.autoLabel | Auto Label | Auto-Beschriftung |
| account.autoSummarizationDisabled | Auto-summarization disabled by admin | Auto-Zusammenfassung von Admin deaktiviert |
| account.autoSummarize | Auto Summarize | Auto-Zusammenfassen |
| account.defaultHotwords | Default Hotwords | Standard-Hotwords |
| account.defaultHotwordsPlaceholder | e.g. Speakr, CTranslate2, PyAnnote, SDRs | z. B. Speakr, CTranslate2, PyAnnote, SDRs |
| account.defaultInitialPrompt | Default Initial Prompt | Standard-Initial-Prompt |
| account.defaultInitialPromptPlaceholder | e.g. This is a meeting about AI transcription tools... | z. B. Dies ist ein Meeting über KI-Transkriptionstools. Die Sprecher diskutieren über CTranslate2, PyAnnote und SDRs. |
| account.personalFolder | Personal folder (not linked to a group) | Persönlicher Ordner (nicht mit einer Gruppe verknüpft) |
| account.personalTag | Personal tag (not linked to a group) | Persönlicher Tag (nicht mit einer Gruppe verknüpft) |
| account.ssoLinkAccount | Link {{provider}} Account | {{provider}}-Konto verknüpfen |
| account.ssoLinked | Linked | Verknüpft |
| account.ssoNotLinked | Not linked | Nicht verknüpft |
| account.ssoProvider | Provider | Anbieter |
| account.ssoSetPasswordFirst | To unlink SSO, please set a password first | Zum Entkoppeln von SSO müssen Sie zuerst ein Passwort festlegen. |
| account.ssoSubject | Subject: | Betreff: |
| account.ssoUnlinkAccount | Unlink {{provider}} Account | {{provider}}-Konto entkoppeln |
| account.ssoUnlinkConfirm | Are you sure you want to unlink your SSO account… | Sind Sie sicher, dass Sie Ihr SSO-Konto entkoppeln möchten? Sie müssen dann Ihr Passwort zum Einloggen verwenden. |
| account.transcriptionHints | Transcription Hints | Transkriptionshinweise |
| account.transcriptionHintsDesc | These defaults are used when no tag or folder overrides are set… | Diese Standardwerte werden verwendet, wenn keine Tag- oder Ordner-Überschreibungen gesetzt sind. Sie helfen, die Transkriptionsgenauigkeit für Ihren spezifischen Anwendungsfall zu verbessern. |

## adminDashboard

| Key | English | German |
|------|---------|--------|
| adminDashboard.admin | ADMIN | ADMIN |
| adminDashboard.allowed | Allowed | Erlaubt |
| adminDashboard.createFirstGroup | Create First Group | Erste Gruppe erstellen |
| adminDashboard.created | Created | Erstellt |
| adminDashboard.description | Description | Beschreibung |
| adminDashboard.groupName | Group Name | Gruppenname |
| adminDashboard.groupsTab | Groups | Gruppen |
| adminDashboard.members | Members | Mitglieder |
| adminDashboard.membersCount | Members | Mitglieder |
| adminDashboard.noDescription | No description | Keine Beschreibung |
| adminDashboard.noGroupsAdmin | You are not an admin of any group yet | Sie sind noch kein Admin einer Gruppe |
| adminDashboard.noGroupsCreated | No groups created yet | Noch keine Gruppen erstellt |
| adminDashboard.noMembersYet | No members yet | Noch keine Mitglieder |
| adminDashboard.passwordsDoNotMatch | Passwords do not match | Passwörter stimmen nicht überein |
| adminDashboard.publicShare | Public Share | Öffentliches Teilen |

## buttons

| Key | English | German |
|------|---------|--------|
| buttons.cancel | Cancel | Abbrechen |
| buttons.close | Close | Schließen |
| buttons.createTag | Create Tag | Tag erstellen |
| buttons.deleteAll | Delete All | Alle löschen |
| buttons.refresh | Refresh | Aktualisieren |
| buttons.saveCustomPrompt | Save Custom Prompt | Benutzerdefinierten Prompt speichern |
| buttons.updateTag | Update Tag | Tag aktualisieren |

## chat

| Key | English | German |
|------|---------|--------|
| chat.cannotChatTranscriptionFailed | Cannot chat: Transcription failed… | Chat nicht möglich: Transkription fehlgeschlagen. Bitte transkribieren Sie die Aufnahme erneut. |
| chat.cleared | Chat cleared | Chat geleert |
| chat.downloadFailed | Chat download failed | Download des Chats fehlgeschlagen |
| chat.downloadSuccess | Chat downloaded successfully! | Chat erfolgreich heruntergeladen! |
| chat.noMessagesToDownload | No chat messages to download | Keine Chat-Nachrichten zum Herunterladen. |
| chat.title | Chat | Chat |

## colorScheme

| Key | English | German |
|------|---------|--------|
| colorScheme.descriptions.amber | Warm amber tones for a cozy feel | Warme Bernsteintöne für ein gemütliches, produktives Gefühl |
| colorScheme.descriptions.blue | Classic blue design with a clean look | Klassisches Blau-Design mit einem sauberen, professionellen Look |
| colorScheme.descriptions.emerald | Nature-inspired green for a calming experience | Naturinspiriertes Grün-Design für ein beruhigendes Erlebnis |
| colorScheme.descriptions.purple | Rich purple with an elegant modern look | Reichhaltiges Lila-Design mit einem eleganten, modernen Look |
| colorScheme.descriptions.rose | Warm rose with a soft inviting aesthetic | Warmes Rosen-Design mit einer sanften, einladenden Ästhetik |
| colorScheme.descriptions.teal | Cool teal with a refreshing modern style | Kühles Türkis-Design mit einem erfrischenden, modernen Stil |
| colorScheme.names.amber | Golden Amber | Goldener Bernstein |
| colorScheme.names.blue | Ocean Blue | Ozeanblau |
| colorScheme.names.emerald | Forest Green | Waldgrün |
| colorScheme.names.purple | Royal Purple | Königspurpur |
| colorScheme.names.rose | Coral Rose | Korallenrose |
| colorScheme.names.teal | Arctic Teal | Arktistürkis |

## editTagModal

| Key | English | German |
|------|---------|--------|
| editTagModal.defaultPromptPlaceholder | Leave empty to use the default summary prompt | Leer lassen, um Ihren Standard-Zusammenfassungs-Prompt zu verwenden |
| editTagModal.watchFolder | Watch Folder | Überwachungsordner |
| editTagModal.watchFolderCreated | Watch folder created | Überwachungsordner erstellt |
| editTagModal.watchFolderError | Could not create watch folder | Überwachungsordner konnte nicht erstellt werden |
| editTagModal.watchFolderGroupTagError | Watch folders are not available for group tags | Überwachungsordner sind für Gruppen-Tags nicht verfügbar |
| editTagModal.watchFolderPath | Drop files in: | Dateien ablegen in: |
| editTagModal.watchFolderRemoved | Watch folder removed | Überwachungsordner entfernt |

## errors

| Key | English | German |
|------|---------|--------|
| errors.audioExtractionFailed | Audio extraction failed | Audio-Extraktion fehlgeschlagen |
| errors.audioExtractionFailedGuidance | Try converting to MP3/WAV | Versuchen Sie, die Datei vor dem Hochladen in ein Standard-Audioformat (MP3, WAV) zu konvertieren. |
| errors.audioExtractionFailedMessage | Could not extract audio from uploaded file | Audio konnte nicht aus der hochgeladenen Datei extrahiert werden. |
| errors.audioRecordingFailed | Audio recording failed | Audioaufnahme fehlgeschlagen. Bitte überprüfen Sie Ihr Mikrofon. |
| errors.authenticationError | Authentication error | Authentifizierungsfehler |
| errors.authenticationErrorGuidance | Check if API key is correct | Bitte überprüfen Sie, ob der API-Schlüssel korrekt und nicht abgelaufen ist. |
| errors.authenticationErrorMessage | The transcription service rejected the API credentials | Der Transkriptionsdienst hat die API-Anmeldedaten abgelehnt. |
| errors.checkApiKeyGuidance | Check API key in settings | API-Schlüssel in den Einstellungen überprüfen |
| errors.checkNetworkGuidance | Check network connection | Netzwerkverbindung überprüfen |
| errors.connectionError | Connection error | Verbindungsfehler |
| errors.connectionErrorGuidance | Check internet connection | Überprüfen Sie Ihre Internetverbindung und stellen Sie sicher, dass der Dienst verfügbar ist. |
| errors.connectionErrorMessage | Could not connect to transcription service | Konnte keine Verbindung zum Transkriptionsdienst herstellen. |
| errors.convertFormatGuidance | Convert to MP3 or WAV before uploading | Vor dem Hochladen in MP3 oder WAV konvertieren |
| errors.convertStandardGuidance | Convert to a standard audio format | In ein Standard-Audioformat konvertieren |
| errors.enableChunkingGuidance | Enable chunking in settings or compress | Chunking in den Einstellungen aktivieren oder die Datei komprimieren |
| errors.fallbackMessage | An error occurred | Ein Fehler ist aufgetreten |
| errors.fallbackTitle | Error | Fehler |
| errors.fileTooLarge | File too large | Datei zu groß |
| errors.fileTooLargeGuidance | Try enabling audio chunking | Versuchen Sie, Audio-Chunking in Ihren Einstellungen zu aktivieren oder die Audiodatei vor dem Hochladen zu komprimieren. |
| errors.fileTooLargeMaxSize | File too large. Max: {{size}} MB | Datei zu groß. Max: {{size}} MB. |
| errors.fileTooLargeMessage | The audio file exceeds the maximum size | Die Audiodatei überschreitet die vom Transkriptionsdienst zugelassene Maximalgröße. |
| errors.fileTooLargeTitle | File too large | Datei zu groß |
| errors.generic | An error occurred | Ein Fehler ist aufgetreten |
| errors.invalidAudioFormat | Invalid audio format | Ungültiges Audioformat |
| errors.invalidAudioFormatGuidance | Try converting to MP3 or WAV | Versuchen Sie, die Audiodatei vor dem Hochladen in MP3 oder WAV zu konvertieren. |
| errors.invalidAudioFormatMessage | Audio format not supported or file corrupted | Das Audioformat wird nicht unterstützt oder die Datei ist möglicherweise beschädigt. |
| errors.networkError | Network error | Netzwerkfehler. Bitte überprüfen Sie Ihre Verbindung. |
| errors.networkErrorDuringUpload | Network error during upload | Netzwerkfehler während des Uploads |
| errors.notFound | Not found | Nicht gefunden |
| errors.permissionDenied | Permission denied | Zugriff verweigert |
| errors.processingError | Processing error | Verarbeitungsfehler |
| errors.processingErrorFallbackGuidance | Try reprocessing the recording | Versuchen Sie, die Aufnahme erneut zu verarbeiten |
| errors.processingErrorGuidance | If this persists, try reprocessing | Wenn dieser Fehler weiterhin besteht, versuchen Sie, die Aufnahme erneut zu verarbeiten. |
| errors.processingErrorMessage | An error occurred during processing | Während der Verarbeitung ist ein Fehler aufgetreten. |
| errors.processingFailedOnServer | Processing failed on server | Verarbeitung auf dem Server fehlgeschlagen. |
| errors.processingFailedWithStatus | Processing failed with status {{status}} | Verarbeitung mit Status {{status}} fehlgeschlagen |
| errors.processingTimeout | Processing timeout | Verarbeitungszeitüberschreitung |
| errors.processingTimeoutGuidance | This can happen with very long recordings | Dies kann bei sehr langen Aufnahmen passieren. Versuchen Sie, die Audiodatei in kleinere Teile aufzuteilen. |
| errors.processingTimeoutMessage | The transcription took too long | Die Transkription hat zu lange gedauert. |
| errors.quotaExceeded | Quota exceeded | Speicherkontingent überschritten |
| errors.rateLimitExceeded | Rate limit exceeded | Ratenlimit überschritten |
| errors.rateLimitExceededGuidance | Please wait a few minutes and retry | Bitte warten Sie einige Minuten und versuchen Sie es erneut. |
| errors.rateLimitExceededMessage | Too many requests to transcription service | Es wurden zu viele Anfragen an den Transkriptionsdienst gesendet. |
| errors.serverErrorStatus | Server error ({{status}}) | Serverfehler ({{status}}) |
| errors.serviceUnavailable | Service unavailable | Dienst nicht verfügbar |
| errors.serviceUnavailableGuidance | This is usually temporary. Please retry. | Dies ist normalerweise vorübergehend. Bitte versuchen Sie es in ein paar Minuten erneut. |
| errors.serviceUnavailableMessage | The transcription service is temporarily unavailable | Der Transkriptionsdienst ist vorübergehend nicht verfügbar. |
| errors.splitAudioGuidance | Try splitting the audio into smaller parts | Versuchen Sie, die Audiodatei in kleinere Teile aufzuteilen |
| errors.summaryFailed | Summary failed | Zusammenfassung fehlgeschlagen. Bitte versuchen Sie es erneut. |
| errors.transcriptionFailed | Transcription failed | Transkription fehlgeschlagen. Bitte versuchen Sie es erneut. |
| errors.tryAgainLaterGuidance | Try again in a few minutes | Versuchen Sie es in ein paar Minuten erneut |
| errors.unauthorized | Unauthorized | Nicht autorisiert |
| errors.unexpectedResponse | Unexpected success response from server | Unerwartete Erfolgsantwort vom Server nach dem Upload. |
| errors.unsupportedFormat | Unsupported format | Nicht unterstütztes Format |
| errors.uploadFailed | Upload failed | Upload fehlgeschlagen. Bitte versuchen Sie es erneut. |
| errors.uploadFailedWithStatus | Upload failed with status {{status}} | Upload mit Status {{status}} fehlgeschlagen |
| errors.uploadTimedOut | Upload timed out | Upload-Zeitüberschreitung |
| errors.validationError | Validation error | Validierungsfehler |
| errors.waitAndRetryGuidance | Wait a few minutes and retry | Einige Minuten warten und erneut versuchen |

## form

| Key | English | German |
|------|---------|--------|
| form.folder | Folder | Ordner |
| form.hotwordsHelp | Comma-separated words to improve recognition of domain-specific terms | Durch Komma getrennte Wörter zur Verbesserung der Erkennung domänenspezifischer Begriffe |
| form.hotwordsPlaceholder | e.g. Speakr, CTranslate2, PyAnnote | z. B. Speakr, CTranslate2, PyAnnote |
| form.initialPrompt | Initial Prompt | Initial-Prompt |
| form.initialPromptHelp | Context to steer the transcription model's style and vocabulary | Kontext zur Steuerung des Stils und Vokabulars des Transkriptionsmodells |
| form.initialPromptPlaceholder | e.g. This is a meeting about AI transcription tools | z. B. Dies ist ein Meeting über KI-Transkriptionstools. |
| form.participantNamePlaceholder | Participant name... | Teilnehmername... |
| form.transcriptionLanguage | Transcription Language | Transkriptionssprache |

## help

| Key | English | German |
|------|---------|--------|
| help.allTagsSelected | All tags selected | Alle Tags ausgewählt |
| help.createFolders | Create folders | Ordner erstellen |
| help.defaultHotwordsHelp | Comma-separated words or phrases that the transcription model should prioritize | Durch Komma getrennte Wörter oder Phrasen, die das Transkriptionsmodell priorisieren soll. |
| help.defaultInitialPromptHelp | Context to steer the transcription model's style and vocabulary | Kontext zur Steuerung des Stils und Vokabulars des Transkriptionsmodells. Beschreiben Sie das Thema für bessere Ergebnisse. |
| help.dragToReorder | Drag to reorder | Zum Umsortieren ziehen |
| help.firstTagAsrSettings | First tag's ASR settings will be applied | ASR-Einstellungen des ersten Tags werden angewendet: |
| help.firstTagDefaultsApplied | First tag's defaults applied | Standardeinstellungen des ersten Tags angewendet |
| help.folderHasCustomPrompt | This folder has a custom summary prompt | Dieser Ordner hat einen benutzerdefinierten Zusammenfassungs-Prompt |
| help.noMatchingTags | No matching tags | Keine passenden Tags |
| help.selectedTagsCustomPrompts | Selected tags include custom summary prompts | Ausgewählte Tags enthalten benutzerdefinierte Zusammenfassungs-Prompts |
| help.startTime | Start | Start |
| help.systemAudioHelp | Record system audio – select this option in your screen sharing dialog | Systemaudio aufnehmen – wählen Sie diesen Eintrag in Ihrem Bildschirmfreigabefenster aus. Stellen Sie sicher, dass Sie \"Tab\" oder \"Bildschirm\" und nicht nur \"Ihren Bildschirm\" auswählen. |
| help.toOrganizeRecordings | to organize your recordings | um Ihre Aufnahmen zu organisieren |

## incognito

| Key | English | German |
|------|---------|--------|
| incognito.audioNotStored | Audio not stored in incognito mode | Audio wird im Inkognito-Modus nicht gespeichert |
| incognito.discardConfirm | This will permanently discard your incognito recording | Dadurch wird Ihre Inkognito-Aufnahme endgültig verworfen. Fortfahren? |
| incognito.mode | Incognito Mode | Inkognito-Modus |
| incognito.notSavedToAccount | Not saved to account | Nicht im Konto gespeichert |
| incognito.oneFileAtATime | Incognito mode supports one file at a time | Der Inkognito-Modus unterstützt nur eine Datei gleichzeitig |
| incognito.processInIncognito | Process in Incognito | Inkognito verarbeiten |
| incognito.processWithoutSaving | Process without saving | Ohne Speichern verarbeiten |
| incognito.processing | Processing... | Verarbeitung läuft... |
| incognito.processingComplete | Processing complete! | Verarbeitung abgeschlossen! |
| incognito.processingInProgress | Processing in incognito mode... | Verarbeitung im Inkognito-Modus... |
| incognito.recordingDiscarded | Incognito recording discarded | Inkognito-Aufnahme verworfen |
| incognito.recordingProcessed | Incognito recording processed – data lost on tab close | Inkognito-Aufnahme verarbeitet – Daten gehen beim Schließen des Tabs verloren |
| incognito.recordingReady | Incognito recording ready! | Inkognito-Aufnahme bereit! |
| incognito.recordingTitle | Incognito recording | Inkognito-Aufnahme |
| incognito.selectExactlyOneFile | Select exactly one file | Wählen Sie genau eine Datei aus |
| incognito.sessionOnly | Session only | Nur für diese Sitzung |
| incognito.uploadingFile | Uploading file for incognito processing... | Datei wird für Inkognito-Verarbeitung hochgeladen... |

## messages

| Key | English | German |
|------|---------|--------|
| messages.beforeunloadRecording | You have an unsaved recording. Are you sure you want to leave? | Sie haben eine ungespeicherte Aufnahme. Möchten Sie die Seite wirklich verlassen? |
| messages.beforeunloadIncognito | You have an incognito recording that will be lost. Are you sure you want to leave? | Sie haben eine Inkognito-Aufnahme, die verloren geht. Möchten Sie die Seite wirklich verlassen? |
| messages.colorSchemeApplied | Color scheme applied | Farbschema angewendet |
| messages.colorSchemeReset | Color scheme reset to default | Farbschema auf Standard zurückgesetzt |
| messages.copiedSuccessfully | Copied to clipboard! | In die Zwischenablage kopiert! |
| messages.copyFailed | Copy failed | Kopieren fehlgeschlagen |
| messages.copyNotSupported | Copy not supported. Your browser may not support this. | Kopieren fehlgeschlagen. Ihr Browser unterstützt diese Funktion möglicherweise nicht. |
| messages.errorRecoveringRecording | Error recovering recording | Fehler beim Wiederherstellen der Aufnahme |
| messages.eventDownloadFailed | Event download failed | Download des Ereignisses fehlgeschlagen |
| messages.eventDownloadSuccess | Event "{{title}}" downloaded. Open the file to add to your calendar. | Ereignis "{{title}}" heruntergeladen. Öffnen Sie die Datei, um sie zu Ihrem Kalender hinzuzufügen. |
| messages.eventsExportFailed | Events export failed | Export der Ereignisse fehlgeschlagen |
| messages.eventsExportSuccess | {{count}} events exported | {{count}} Ereignisse exportiert |
| messages.failedToDeleteJob | Failed to delete job | Löschen des Auftrags fehlgeschlagen |
| messages.failedToRecoverRecording | Failed to recover recording | Wiederherstellen der Aufnahme fehlgeschlagen |
| messages.failedToRetryJob | Failed to retry job | Wiederholen des Auftrags fehlgeschlagen |
| messages.failedToSave | Failed to save: {{error}} | Speichern fehlgeschlagen: {{error}} |
| messages.failedToSaveParticipants | Failed to save participants | Speichern der Teilnehmer fehlgeschlagen |
| messages.followPlayerDisabled | Follow player mode disabled | Follow-Player-Modus deaktiviert |
| messages.followPlayerEnabled | Follow player mode enabled | Follow-Player-Modus aktiviert |
| messages.invalidEventData | Invalid event data | Ungültige Ereignisdaten |
| messages.jobQueuedForRetry | Job queued for retry | Auftrag zur Wiederholung eingereiht |
| messages.noEventsToExport | No events to export | Keine Ereignisse zum Exportieren |
| messages.noNotesAvailableDownload | No notes available for download | Keine Notizen zum Herunterladen verfügbar. |
| messages.noNotesToCopy | No notes to copy | Keine Notizen zum Kopieren verfügbar. |
| messages.noPermissionToEdit | You don't have permission to edit this recording | Sie haben keine Berechtigung, diese Aufnahme zu bearbeiten |
| messages.noSummaryToCopy | No summary to copy | Keine Zusammenfassung zum Kopieren verfügbar. |
| messages.noSummaryToDownload | No summary available for download | Keine Zusammenfassung zum Herunterladen verfügbar. |
| messages.noTranscriptionToCopy | No transcription to copy | Keine Transkription zum Kopieren verfügbar. |
| messages.noTranscriptionToDownload | No transcription available for download | Keine Transkription zum Herunterladen verfügbar. |
| messages.notesCopied | Notes copied to clipboard! | Notizen in die Zwischenablage kopiert! |
| messages.notesDownloadFailed | Notes download failed | Download der Notizen fehlgeschlagen |
| messages.notesDownloadSuccess | Notes downloaded successfully! | Notizen erfolgreich heruntergeladen! |
| messages.recordingDiscarded | Recording discarded | Aufnahme verworfen |
| messages.recordingRecovered | Recording recovered successfully | Aufnahme erfolgreich wiederhergestellt |
| messages.saveParticipantsFailed | Save failed: {{error}} | Speichern fehlgeschlagen: {{error}} |
| messages.summaryCopied | Summary copied to clipboard! | Zusammenfassung in die Zwischenablage kopiert! |
| messages.summaryDownloadFailed | Summary download failed | Download der Zusammenfassung fehlgeschlagen |
| messages.summaryDownloadSuccess | Summary downloaded successfully! | Zusammenfassung erfolgreich heruntergeladen! |
| messages.transcriptDownloadFailed | Transcript download failed | Download des Transkripts fehlgeschlagen |
| messages.transcriptDownloadSuccess | Transcript downloaded successfully! | Transkript erfolgreich heruntergeladen! |
| messages.transcriptionCopied | Transcription copied to clipboard! | Transkription in die Zwischenablage kopiert! |

## recording

| Key | English | German |
|------|---------|--------|
| recording.micPlusSys | Mic + System | Mikro + System |

## sharing

| Key | English | German |
|------|---------|--------|
| sharing.teamBadge | Team | Gruppe |

## tooltips

| Key | English | German |
|------|---------|--------|
| tooltips.exitFullscreen | Exit Fullscreen | Vollbild beenden |
| tooltips.fullscreenVideo | Fullscreen Video | Video im Vollbild |
| tooltips.hideVideo | Hide Video | Video ausblenden |
| tooltips.showVideo | Show Video | Video einblenden |

## upload

| Key | English | German |
|------|---------|--------|
| upload.fileExceedsMaxSize | File "{{name}}" exceeds max size of {{size}} MB and was skipped. | Datei "{{name}}" überschreitet die maximale Größe von {{size}} MB und wurde übersprungen. |
| upload.fileRemovedFromQueue | File removed from queue | Datei aus der Warteschlange entfernt |
| upload.filesToUpload | Files to upload | Dateien zum Hochladen |
| upload.invalidFileType | Invalid file type "{{name}}". Only audio files and video containers (MP3, WAV, M4A, MP4, WebM, OGG, FLAC) are supported. | Ungültiger Dateityp "{{name}}". Nur Audiodateien und Video-Container mit Audio (MP3, WAV, M4A, MP4, WebM, OGG, FLAC) werden unterstützt. |
| upload.settingsApplyToAll | Settings apply to all files in this session | Einstellungen gelten für alle Dateien in dieser Sitzung |
| upload.uploadNFiles | Upload {{count}} file(s) | {{count}} Datei(en) hochladen |

---

## New keys to add to both en.json AND de.json

These are toast messages currently used as raw JS strings. Add them to both locale files.

### toasts

| Key | English (en.json) | German (de.json) |
|------|-------------------|-------------------|
| toasts.apiTokenCreated | API token created successfully | API-Token erfolgreich erstellt |
| toasts.accountUpdated | Account information updated successfully | Kontoinformationen erfolgreich aktualisiert |
| toasts.customPromptSaved | Custom prompt saved successfully | Benutzerdefinierter Prompt erfolgreich gespeichert |
| toasts.exportTemplateCreated | Default export template created successfully | Standard-Exportvorlage erfolgreich erstellt |
| toasts.namingTemplateUpdated | Default naming template updated | Standard-Benennungsvorlage aktualisiert |
| toasts.namingTemplatesCreated | Default naming templates created | Standard-Benennungsvorlagen erstellt |
| toasts.defaultTemplatesCreated | Default templates created successfully | Standardvorlagen erfolgreich erstellt |
| toasts.enterModelId | Enter the model id (e.g. whisper-1, large-v3, voxtral-mini-latest): | Modell-ID eingeben (z. B. whisper-1, large-v3, voxtral-mini-latest): |
| toasts.errorDeletingShare | Error deleting share. | Fehler beim Löschen der Freigabe. |
| toasts.errorUpdatingShare | Error updating share. | Fehler beim Aktualisieren der Freigabe. |
| toasts.failedPushNotificationsConfig | Failed to configure push notifications | Push-Benachrichtigungen konnten nicht konfiguriert werden |
| toasts.failedCopyToken | Failed to copy token to clipboard | Token konnte nicht in die Zwischenablage kopiert werden |
| toasts.failedCreateExportTemplate | Failed to create default export template | Standard-Exportvorlage konnte nicht erstellt werden |
| toasts.failedCreateNamingTemplates | Failed to create default naming templates | Standard-Benennungsvorlagen konnten nicht erstellt werden |
| toasts.failedCreateTemplates | Failed to create default templates | Standardvorlagen konnten nicht erstellt werden |
| toasts.failedCreateToken | Failed to create token: | Token konnte nicht erstellt werden: |
| toasts.failedDeleteExportTemplate | Failed to delete export template | Exportvorlage konnte nicht gelöscht werden |
| toasts.failedDeleteFolder | Failed to delete folder: | Ordner konnte nicht gelöscht werden: |
| toasts.failedDeleteTemplate | Failed to delete template | Vorlage konnte nicht gelöscht werden |
| toasts.failedDisablePush | Failed to disable push notifications | Push-Benachrichtigungen konnten nicht deaktiviert werden |
| toasts.failedEnablePush | Failed to enable push notifications | Push-Benachrichtigungen konnten nicht aktiviert werden |
| toasts.failedLoadExportTemplates | Failed to load export templates | Exportvorlagen konnten nicht geladen werden |
| toasts.failedLoadNamingTemplates | Failed to load naming templates | Benennungsvorlagen konnten nicht geladen werden |
| toasts.failedLoadTemplates | Failed to load templates | Vorlagen konnten nicht geladen werden |
| toasts.failedRevokeToken | Failed to revoke token: | Token konnte nicht widerrufen werden: |
| toasts.failedSaveCustomPrompt | Failed to save custom prompt | Benutzerdefinierter Prompt konnte nicht gespeichert werden |
| toasts.failedSaveFolder | Failed to save folder: | Ordner konnte nicht gespeichert werden: |
| toasts.failedSavePreferences | Failed to save preferences | Einstellungen konnten nicht gespeichert werden |
| toasts.failedTestTemplate | Failed to test template | Vorlage konnte nicht getestet werden |
| toasts.failedUpdateAccount | Failed to update account information | Kontoinformationen konnten nicht aktualisiert werden |
| toasts.failedUpdateDefaultTemplate | Failed to update default template | Standardvorlage konnte nicht aktualisiert werden |
| toasts.failedUpdateLanguage | Failed to update language. Please try again. | Sprache konnte nicht aktualisiert werden. Bitte versuchen Sie es erneut. |
| toasts.failedUpdateToken | Failed to update token: | Token konnte nicht aktualisiert werden: |
| toasts.folderNameRequired | Folder name is required | Ordnername ist erforderlich |
| toasts.folderPrefix | Folder | Ordner |
| toasts.incognitoRecordingLost | Incognito recording processed - data will be lost when tab closes | Inkognito-Aufnahme verarbeitet – Daten gehen beim Schließen des Tabs verloren |
| toasts.installingSpeakr | Installing Speakr... | Speakr wird installiert... |
| toasts.meetingDateUpdated | Meeting date updated! | Meeting-Datum aktualisiert! |
| toasts.namingTemplateDeleted | Naming template deleted | Benennungsvorlage gelöscht |
| toasts.networkError | Network error: | Netzwerkfehler: |
| toasts.passwordMismatch | New password and confirmation do not match. | Das neue Passwort und die Bestätigung stimmen nicht überein. |
| toasts.noAudioTrack | No audio track - check | Keine Audiospur – überprüfen Sie |
| toasts.noSourceSpeakers | No source speakers to merge | Keine Quell-Sprecher zum Zusammenführen |
| toasts.notesCopied | Notes copied to clipboard! | Notizen in die Zwischenablage kopiert! |
| toasts.notesSavedBrowser | Notes saved (in browser only) | Notizen gespeichert (nur im Browser) |
| toasts.notesSaved | Notes saved! | Notizen gespeichert! |
| toasts.notificationDenied | Notification permission denied | Benachrichtigungsberechtigung verweigert |
| toasts.notificationsEnabled | Notifications enabled | Benachrichtigungen aktiviert |
| toasts.enterTokenName | Please enter a token name | Bitte geben Sie einen Token-Namen ein |
| toasts.selectMinSpeakers | Please select at least 2 speakers to merge | Bitte wählen Sie mindestens 2 Sprecher zum Zusammenführen aus |
| toasts.selectSpeakersClear | Please select speakers to clear voice profiles | Bitte wählen Sie Sprecher zum Löschen der Sprachprofile aus |
| toasts.selectSpeakersDelete | Please select speakers to delete | Bitte wählen Sie zu löschende Sprecher aus |
| toasts.selectSpeakerKeep | Please select which speaker to keep | Bitte wählen Sie den zu behaltenden Sprecher aus |
| toasts.preferencesSaved | Preferences saved | Einstellungen gespeichert |
| toasts.processingCompleted | Processing completed! | Verarbeitung abgeschlossen! |
| toasts.processingFailed | Processing failed | Verarbeitung fehlgeschlagen |
| toasts.pushDenied | Push notification permission denied | Push-Benachrichtigungsberechtigung verweigert |
| toasts.pushDisabled | Push notifications disabled | Push-Benachrichtigungen deaktiviert |
| toasts.pushEnabled | Push notifications enabled | Push-Benachrichtigungen aktiviert |
| toasts.pushNotAvailable | Push notifications not available. Install pywebpush on server. | Push-Benachrichtigungen nicht verfügbar. Installieren Sie pywebpush auf dem Server. |
| toasts.pushNotSupported | Push notifications not supported in this browser | Push-Benachrichtigungen werden in diesem Browser nicht unterstützt |
| toasts.recordingArchived | Recording archived (audio deleted) | Aufnahme archiviert (Audio gelöscht) |
| toasts.recordingDeleted | Recording deleted. | Aufnahme gelöscht. |
| toasts.recordingReset | Recording reset for reprocessing. | Aufnahme für erneute Verarbeitung zurückgesetzt. |
| toasts.recordingResumed | Recording resumed - screen will stay awake | Aufnahme fortgesetzt – Bildschirm bleibt wach |
| toasts.recordingStatusReset | Recording status reset to FAILED | Aufnahmestatus auf FEHLGESCHLAGEN zurückgesetzt |
| toasts.recordingUpdated | Recording updated! | Aufnahme aktualisiert! |
| toasts.removedFromFolder | Removed from folder | Aus Ordner entfernt |
| toasts.saveTemplateFirst | Save the template first to test it | Speichern Sie die Vorlage zuerst, um sie zu testen |
| toasts.screenLockDenied | Screen lock permission denied | Bildschirmsperrberechtigung verweigert |
| toasts.screenMaySleep | Screen may sleep during recording | Bildschirm kann während der Aufnahme in den Ruhezustand gehen |
| toasts.screenSharingCancelled | Screen sharing was cancelled | Bildschirmfreigabe wurde abgebrochen |
| toasts.shareDeleted | Share deleted successfully | Freigabe erfolgreich gelöscht |
| toasts.shareLinkCopied | Share link copied to clipboard | Freigabelink in die Zwischenablage kopiert |
| toasts.shareLinkCreated | Share link created successfully! | Freigabelink erfolgreich erstellt! |
| toasts.shareLinkDeleted | Share link deleted successfully. | Freigabelink erfolgreich gelöscht. |
| toasts.sharePermissionsUpdated | Share permissions updated. | Freigabeberechtigungen aktualisiert. |
| toasts.speakerNameUpdated | Speaker name updated successfully | Sprechername erfolgreich aktualisiert |
| toasts.speakrInstalled | Speakr installed successfully! | Speakr erfolgreich installiert! |
| toasts.summaryCopied | Summary copied to clipboard! | Zusammenfassung in die Zwischenablage kopiert! |
| toasts.summaryGenerated | Summary generated | Zusammenfassung erstellt |
| toasts.summaryGenerationStarted | Summary generation started | Zusammenfassungserstellung gestartet |
| toasts.summaryReprocessingStarted | Summary reprocessing started | Erneute Zusammenfassungserstellung gestartet |
| toasts.summarySaved | Summary saved! | Zusammenfassung gespeichert! |
| toasts.tagAdded | Tag added successfully | Tag erfolgreich hinzugefügt |
| toasts.tagAddedExcl | Tag added! | Tag hinzugefügt! |
| toasts.tagRemoved | Tag removed successfully | Tag erfolgreich entfernt |
| toasts.tagRemovedExcl | Tag removed! | Tag entfernt! |
| toasts.tagsReordered | Tags reordered | Tags neu angeordnet |
| toasts.exportTemplateDeleted | Export template deleted successfully | Exportvorlage erfolgreich gelöscht |
| toasts.templateDeleted | Template deleted successfully | Vorlage erfolgreich gelöscht |
| toasts.titleRegenerated | Title regenerated | Titel neu generiert |
| toasts.tokenCopied | Token copied to clipboard | Token in die Zwischenablage kopiert |
| toasts.tokenNameEmpty | Token name cannot be empty | Token-Name darf nicht leer sein |
| toasts.tokenNameUpdated | Token name updated | Token-Name aktualisiert |
| toasts.tokenRevoked | Token revoked successfully | Token erfolgreich widerrufen |
| toasts.transcriptionCopied | Transcription copied to clipboard! | Transkription in die Zwischenablage kopiert! |
| toasts.transcriptionReprocessingStarted | Transcription reprocessing started | Erneute Transkription gestartet |
| toasts.transcriptionUpdated | Transcription updated successfully! | Transkription erfolgreich aktualisiert! |
| toasts.usingExistingShareLink | Using existing share link | Vorhandenen Freigabelink verwenden |
| toasts.wakeLockNotSupported | Wake lock not supported on this device | Wake-Lock wird auf diesem Gerät nicht unterstützt |
| toasts.iOSWakeLockIssue | iOS wake lock may not work - keep screen active | iOS Wake-Lock funktioniert möglicherweise nicht – Bildschirm aktiv halten |
