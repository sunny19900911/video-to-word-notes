# Source and transcription guide

## Source resolution

- **Local file:** verify the exact path and media duration, then process it directly.
- **Public video page:** prefer official subtitles. If none exist, download only when the user is authorized and the platform permits it.
- **Logged-in page:** use the user's existing browser session when available. Never request, expose, or store passwords, cookies, tokens, or signed URLs.
- **Cloud drive:** if direct download is unavailable, ask the user to download the video to a local folder. Do not automate CAPTCHA or bypass access controls.
- **Unsupported stream:** explain the limitation and request a local MP4/MOV/MKV/WebM or an audio file.

## Transcription priority

1. Human-authored subtitle matching the actual audio.
2. Platform auto-caption checked against the audio.
3. Local Whisper or another user-authorized speech-to-text engine.

For Whisper, use a model proportionate to the recording quality and available compute. Preserve a timestamped SRT or JSON as an internal intermediate so the final three time ranges can be grounded, but do not expose line-by-line timestamps in the Word body.

## Cleaning rules

- Remove filler only when meaning is unchanged.
- Repair obvious sentence boundaries and repeated false starts.
- Keep names, figures, quotations, conditions, and negations.
- Mark inaudible or uncertain phrases as `[听不清]` or `[uncertain]`.
- Do not silently translate technical names that are clearer in English.

## English-video rule

Create the document in this order:

1. Chinese conclusion, summary, and structured notes.
2. Full Chinese translation when requested or when the user is validating translation quality.
3. Exactly three broad time ranges with Chinese summaries.
4. Complete cleaned English transcript as the final appendix.

Do not interleave English and Chinese sentence by sentence unless the user explicitly asks for a bilingual layout.
