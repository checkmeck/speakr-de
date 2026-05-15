# Übersetzungs-Audit: Speakr Deutsche Lokalisierung

## Zusammenfassung

- **Keys in en.json:** 1395
- **Keys in de.json:** 1395
- **Vollständig fehlende Keys:** 0 (Struktur ist synchron)
- **Unübersetzte Keys (Englisch in de.json):** 248
- **Chinesische Textreste in de.json:** 14
- **Im Code verwendete Keys ohne Locale-Eintrag:** 146

---

## 1. Unübersetzte Keys (englischer Text in de.json)

Insgesamt **248** Keys haben in de.json denselben englischen Wert wie in en.json. Diese werden im UI weiterhin auf Englisch angezeigt.

### aboutPage (6 Keys)

- `aboutPage.backend`
- `aboutPage.dockerHub`
- `aboutPage.frontend`
- `aboutPage.githubRepository`
- `aboutPage.version`
- `aboutPage.whisperApi`

### aboutPageDetails (2 Keys)

- `aboutPageDetails.backend`
- `aboutPageDetails.frontend`

### account (19 Keys)

- `account.autoLabel`
- `account.autoSummarizationDisabled`
- `account.autoSummarize`
- `account.defaultHotwords`
- `account.defaultHotwordsPlaceholder`
- `account.defaultInitialPrompt`
- `account.defaultInitialPromptPlaceholder`
- `account.personalFolder`
- `account.personalTag`
- `account.ssoLinkAccount`
- `account.ssoLinked`
- `account.ssoNotLinked`
- `account.ssoProvider`
- `account.ssoSetPasswordFirst`
- `account.ssoSubject`
- `account.ssoUnlinkAccount`
- `account.ssoUnlinkConfirm`
- `account.transcriptionHints`
- `account.transcriptionHintsDesc`

### adminDashboard (17 Keys)

- `adminDashboard.admin`
- `adminDashboard.allowed`
- `adminDashboard.createFirstGroup`
- `adminDashboard.created`
- `adminDashboard.description`
- `adminDashboard.groupName`
- `adminDashboard.groupsTab`
- `adminDashboard.id`
- `adminDashboard.megabytes`
- `adminDashboard.members`
- `adminDashboard.membersCount`
- `adminDashboard.noDescription`
- `adminDashboard.noGroupsAdmin`
- `adminDashboard.noGroupsCreated`
- `adminDashboard.noMembersYet`
- `adminDashboard.passwordsDoNotMatch`
- `adminDashboard.publicShare`

### buttons (7 Keys)

- `buttons.cancel`
- `buttons.close`
- `buttons.createTag`
- `buttons.deleteAll`
- `buttons.refresh`
- `buttons.saveCustomPrompt`
- `buttons.updateTag`

### chat (6 Keys)

- `chat.cannotChatTranscriptionFailed`
- `chat.cleared`
- `chat.downloadFailed`
- `chat.downloadSuccess`
- `chat.noMessagesToDownload`
- `chat.title`

### colorScheme (12 Keys)

- `colorScheme.descriptions.amber`
- `colorScheme.descriptions.blue`
- `colorScheme.descriptions.emerald`
- `colorScheme.descriptions.purple`
- `colorScheme.descriptions.rose`
- `colorScheme.descriptions.teal`
- `colorScheme.names.amber`
- `colorScheme.names.blue`
- `colorScheme.names.emerald`
- `colorScheme.names.purple`
- `colorScheme.names.rose`
- `colorScheme.names.teal`

### common (3 Keys)

- `common.filter`
- `common.info`
- `common.ok`

### editTagModal (7 Keys)

- `editTagModal.defaultPromptPlaceholder`
- `editTagModal.watchFolder`
- `editTagModal.watchFolderCreated`
- `editTagModal.watchFolderError`
- `editTagModal.watchFolderGroupTagError`
- `editTagModal.watchFolderPath`
- `editTagModal.watchFolderRemoved`

### errors (59 Keys)

- `errors.audioExtractionFailed`
- `errors.audioExtractionFailedGuidance`
- `errors.audioExtractionFailedMessage`
- `errors.audioRecordingFailed`
- `errors.authenticationError`
- `errors.authenticationErrorGuidance`
- `errors.authenticationErrorMessage`
- `errors.checkApiKeyGuidance`
- `errors.checkNetworkGuidance`
- `errors.connectionError`
- `errors.connectionErrorGuidance`
- `errors.connectionErrorMessage`
- `errors.convertFormatGuidance`
- `errors.convertStandardGuidance`
- `errors.enableChunkingGuidance`
- `errors.fallbackMessage`
- `errors.fallbackTitle`
- `errors.fileTooLarge`
- `errors.fileTooLargeGuidance`
- `errors.fileTooLargeMaxSize`
- `errors.fileTooLargeMessage`
- `errors.fileTooLargeTitle`
- `errors.generic`
- `errors.invalidAudioFormat`
- `errors.invalidAudioFormatGuidance`
- `errors.invalidAudioFormatMessage`
- `errors.networkError`
- `errors.networkErrorDuringUpload`
- `errors.notFound`
- `errors.permissionDenied`
- `errors.processingError`
- `errors.processingErrorFallbackGuidance`
- `errors.processingErrorGuidance`
- `errors.processingErrorMessage`
- `errors.processingFailedOnServer`
- `errors.processingFailedWithStatus`
- `errors.processingTimeout`
- `errors.processingTimeoutGuidance`
- `errors.processingTimeoutMessage`
- `errors.quotaExceeded`
- `errors.rateLimitExceeded`
- `errors.rateLimitExceededGuidance`
- `errors.rateLimitExceededMessage`
- `errors.serverErrorStatus`
- `errors.serviceUnavailable`
- `errors.serviceUnavailableGuidance`
- `errors.serviceUnavailableMessage`
- `errors.splitAudioGuidance`
- `errors.summaryFailed`
- `errors.transcriptionFailed`
- `errors.tryAgainLaterGuidance`
- `errors.unauthorized`
- `errors.unexpectedResponse`
- `errors.unsupportedFormat`
- `errors.uploadFailed`
- `errors.uploadFailedWithStatus`
- `errors.uploadTimedOut`
- `errors.validationError`
- `errors.waitAndRetryGuidance`

### exportLabels (1 Keys)

- `exportLabels.tags`

### exportTemplates (1 Keys)

- `exportTemplates.tabTitle`

### fileSize (4 Keys)

- `fileSize.bytes`
- `fileSize.gigabytes`
- `fileSize.kilobytes`
- `fileSize.megabytes`

### form (13 Keys)

- `form.auto`
- `form.folder`
- `form.hotwords`
- `form.hotwordsHelp`
- `form.hotwordsPlaceholder`
- `form.initialPrompt`
- `form.initialPromptHelp`
- `form.initialPromptPlaceholder`
- `form.optional`
- `form.participantNamePlaceholder`
- `form.placeholderAuto`
- `form.placeholderOptional`
- `form.transcriptionLanguage`

### help (13 Keys)

- `help.allTagsSelected`
- `help.autoIdentifyMobile`
- `help.createFolders`
- `help.defaultHotwordsHelp`
- `help.defaultInitialPromptHelp`
- `help.dragToReorder`
- `help.firstTagAsrSettings`
- `help.firstTagDefaultsApplied`
- `help.folderHasCustomPrompt`
- `help.noMatchingTags`
- `help.selectedTagsCustomPrompts`
- `help.startTime`
- `help.toOrganizeRecordings`

### incognito (17 Keys)

- `incognito.audioNotStored`
- `incognito.discardConfirm`
- `incognito.mode`
- `incognito.notSavedToAccount`
- `incognito.oneFileAtATime`
- `incognito.processInIncognito`
- `incognito.processWithoutSaving`
- `incognito.processing`
- `incognito.processingComplete`
- `incognito.processingInProgress`
- `incognito.recordingDiscarded`
- `incognito.recordingProcessed`
- `incognito.recordingReady`
- `incognito.recordingTitle`
- `incognito.selectExactlyOneFile`
- `incognito.sessionOnly`
- `incognito.uploadingFile`

### inquire (1 Keys)

- `inquire.tags`

### languages (1 Keys)

- `languages.hi`

### messages (39 Keys)

- `messages.colorSchemeApplied`
- `messages.colorSchemeReset`
- `messages.copiedSuccessfully`
- `messages.copyFailed`
- `messages.copyNotSupported`
- `messages.errorRecoveringRecording`
- `messages.eventDownloadFailed`
- `messages.eventDownloadSuccess`
- `messages.eventsExportFailed`
- `messages.eventsExportSuccess`
- `messages.failedToDeleteJob`
- `messages.failedToRecoverRecording`
- `messages.failedToRetryJob`
- `messages.failedToSave`
- `messages.failedToSaveParticipants`
- `messages.followPlayerDisabled`
- `messages.followPlayerEnabled`
- `messages.invalidEventData`
- `messages.jobQueuedForRetry`
- `messages.noEventsToExport`
- `messages.noNotesAvailableDownload`
- `messages.noNotesToCopy`
- `messages.noPermissionToEdit`
- `messages.noSummaryToCopy`
- `messages.noSummaryToDownload`
- `messages.noTranscriptionToCopy`
- `messages.noTranscriptionToDownload`
- `messages.notesCopied`
- `messages.notesDownloadFailed`
- `messages.notesDownloadSuccess`
- `messages.recordingDiscarded`
- `messages.recordingRecovered`
- `messages.saveParticipantsFailed`
- `messages.summaryCopied`
- `messages.summaryDownloadFailed`
- `messages.summaryDownloadSuccess`
- `messages.transcriptDownloadFailed`
- `messages.transcriptDownloadSuccess`
- `messages.transcriptionCopied`

### metadata (1 Keys)

- `metadata.status`

### recording (2 Keys)

- `recording.micPlusSys`
- `recording.pauseRecording`

### sharing (1 Keys)

- `sharing.teamBadge`

### sidebar (2 Keys)

- `sidebar.starred`
- `sidebar.tags`

### tagManagement (2 Keys)

- `tagManagement.maxSpeakers`
- `tagManagement.minSpeakers`

### tags (1 Keys)

- `tags.title`

### tooltips (5 Keys)

- `tooltips.exitFullscreen`
- `tooltips.fullscreenVideo`
- `tooltips.hideVideo`
- `tooltips.pause`
- `tooltips.showVideo`

### upload (6 Keys)

- `upload.fileExceedsMaxSize`
- `upload.fileRemovedFromQueue`
- `upload.filesToUpload`
- `upload.invalidFileType`
- `upload.settingsApplyToAll`
- `upload.uploadNFiles`

---

## 2. Chinesische Textreste in de.json

**14** Keys enthalten in de.json chinesischen Text – vermutlich aus einer anderen Locale-Datei (zh.json) übernommen.

- `errors.audioRecordingFailed`
  - DE: "音频录制失败。请检查您的麦克风。"
  - EN: "音频录制失败。请检查您的麦克风。"

- `errors.fileTooLarge`
  - DE: "文件太大"
  - EN: "文件太大"

- `errors.generic`
  - DE: "发生错误"
  - EN: "发生错误"

- `errors.networkError`
  - DE: "网络错误。请检查您的连接。"
  - EN: "网络错误。请检查您的连接。"

- `errors.notFound`
  - DE: "未找到"
  - EN: "未找到"

- `errors.permissionDenied`
  - DE: "权限被拒绝"
  - EN: "权限被拒绝"

- `errors.quotaExceeded`
  - DE: "存储配额已超出"
  - EN: "存储配额已超出"

- `errors.serverError`
  - DE: "服务器错误。请稍后重试。"
  - EN: "Server error ({{status}}): Response was not JSON"

- `errors.summaryFailed`
  - DE: "摘要生成失败。请重试。"
  - EN: "摘要生成失败。请重试。"

- `errors.transcriptionFailed`
  - DE: "转录失败。请重试。"
  - EN: "转录失败。请重试。"

- `errors.unauthorized`
  - DE: "未授权"
  - EN: "未授权"

- `errors.unsupportedFormat`
  - DE: "不支持的文件格式"
  - EN: "不支持的文件格式"

- `errors.uploadFailed`
  - DE: "上传失败。请重试。"
  - EN: "上传失败。请重试。"

- `errors.validationError`
  - DE: "验证错误"
  - EN: "验证错误"

---

## 3. Im Code verwendete Keys ohne Locale-Eintrag

**146** Keys werden im Code mit `_t()` oder `t()` aufgerufen, haben aber **keinen Eintrag in en.json oder de.json**. Das UI zeigt in diesem Fall den rohen Key-Namen an.

### Toast/Notification-Nachrichten (direkt im JS als String)

Diese werden vermutlich als **Alert/Toast-Strings** ausgegeben und müssten entweder in en.json/de.json als Key angelegt oder im Code mit `_t()` übersetzt werden.

- `API token created successfully`
- `Account information updated successfully`
- `Custom prompt saved successfully`
- `Default export template created successfully`
- `Default naming template updated`
- `Default naming templates created`
- `Default templates created successfully`
- `Enter the model id (e.g. whisper-1, large-v3, voxtral-mini-latest):`
- `Error deleting share.`
- `Error updating share.`
- `Failed to configure push notifications`
- `Failed to copy token to clipboard`
- `Failed to create default export template`
- `Failed to create default naming templates`
- `Failed to create default templates`
- `Failed to create token: `
- `Failed to delete export template`
- `Failed to delete folder: `
- `Failed to delete template`
- `Failed to disable push notifications`
- `Failed to enable push notifications`
- `Failed to load export templates`
- `Failed to load naming templates`
- `Failed to load templates`
- `Failed to revoke token: `
- `Failed to save custom prompt`
- `Failed to save folder: `
- `Failed to save preferences`
- `Failed to test template`
- `Failed to update account information`
- `Failed to update default template`
- `Failed to update language. Please try again.`
- `Failed to update token: `
- `Folder `
- `Folder name is required`
- `Incognito recording processed - data will be lost when tab closes`
- `Installing Speakr...`
- `Meeting date updated!`
- `Naming template deleted`
- `Network error: `
- `New password and confirmation do not match.`
- `No audio track - check `
- `No source speakers to merge`
- `Notes copied to clipboard!`
- `Notes saved (in browser only)`
- `Notes saved!`
- `Notification permission denied`
- `Notifications enabled`
- `Please enter a token name`
- `Please select at least 2 speakers to merge`
- `Please select speakers to clear voice profiles`
- `Please select speakers to delete`
- `Please select which speaker to keep`
- `Preferences saved`
- `Processing completed!`
- `Processing failed`
- `Push notification permission denied`
- `Push notifications disabled`
- `Push notifications enabled`
- `Push notifications not available. Install pywebpush on server.`
- `Push notifications not supported in this browser`
- `Recording archived (audio deleted)`
- `Recording deleted.`
- `Recording reset for reprocessing.`
- `Recording resumed - screen will stay awake`
- `Recording status reset to FAILED`
- `Recording updated!`
- `Removed from folder`
- `Save the template first to test it`
- `Screen lock permission denied`
- `Screen may sleep during recording`
- `Screen sharing was cancelled`
- `Share deleted successfully`
- `Share link copied to clipboard`
- `Share link copied to clipboard!`
- `Share link created successfully!`
- `Share link deleted successfully.`
- `Share permissions updated.`
- `Speaker name updated successfully`
- `Speakr installed successfully!`
- `Summary copied to clipboard!`
- `Summary generated`
- `Summary generation started`
- `Summary reprocessing started`
- `Summary saved!`
- `Tag added successfully`
- `Tag added!`
- `Tag removed successfully`
- `Tag removed!`
- `Tags reordered`
- `Title regenerated`
- `Token copied to clipboard`
- `Token name cannot be empty`
- `Token name updated`
- `Token revoked successfully`
- `Transcription copied to clipboard!`
- `Transcription reprocessing started`
- `Transcription updated successfully!`
- `Using existing share link`
- `Wake lock not supported on this device`

### Sonstige

- `,`
- `-`
- `2d`
- `;`
- `Content-Disposition`
- `Export template deleted successfully`
- `T`
- `Template deleted successfully`
- `\n`
- `a`
- `button`
- `colorScheme.themes.`
- `content-disposition`
- `content-type`
- `custom_prompt`
- `default_hotwords`
- `default_initial_prompt`
- `default_language`
- `default_max_speakers`
- `default_min_speakers`
- `default_transcription_model`
- `div`
- `export_template_id`
- `folderTranscriptionModel`
- `group_id`
- `h3`
- `h4`
- `help.systemAudioHelp`
- `i`
- `iOS wake lock may not work - keep screen active`
- `input`
- `input[type=`
- `language-changed`
- `localeChanged`
- `meeting_date`
- `naming_template_id`
- `option`
- `p`
- `q`
- `retention_days`
- `sort_by`
- `span`
- `status.pending`
- `tagTranscriptionModel`
- `tag_id`
- `textarea`

