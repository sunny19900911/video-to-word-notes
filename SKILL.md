---
name: video-to-word-notes
description: Turn local or user-authorized online videos into polished, mobile-readable Word notes. Use when the user asks to transcribe, translate, summarize, or convert a YouTube, Bilibili, Haokan, cloud-drive, or local video into Chinese notes or a .docx; for English videos, put Chinese content first and append the complete English transcript, and keep timestamps out of the body except for a final three-part overview.
---

# Video to Word Notes

Create a faithful transcript first, then derive readable notes. Treat summaries as transformations of the source, never as replacements for transcription accuracy.

## Workflow

1. Resolve the source.
   - Prefer a local video path.
   - For an authorized public URL, use available captions or a downloader such as `yt-dlp`.
   - For login-gated or cloud-drive content, use the user's existing authorized session or ask them to download the video locally. Never bypass access controls.
   - Read [references/source-and-transcription.md](references/source-and-transcription.md) when the source is not already local.
2. Extract speech audio.
   - Run `scripts/extract_audio.py` to create mono 16 kHz PCM WAV.
   - Keep the source video unchanged.
3. Transcribe before summarizing.
   - Prefer supplied subtitles when they match the spoken audio.
   - Otherwise use a local Whisper implementation or an authorized transcription service.
   - Preserve names, numbers, examples, qualifications, and speaker intent. Mark uncertain wording instead of inventing it.
4. Detect the spoken language.
   - Chinese video: produce Chinese notes.
   - English video: translate the full meaning into natural Chinese, use Chinese for all main notes, and append the complete cleaned English transcript.
   - Mixed-language video: keep essential original terms in parentheses after the Chinese translation.
5. Structure the content according to [references/notes-schema.md](references/notes-schema.md).
   - Omit line-by-line timestamps from headings and paragraphs.
   - Include exactly three broad time ranges near the end.
   - Separate source claims from the note writer's inference. Do not diagnose people or overstate weak evidence.
6. Generate the Word file.
   - Invoke the `documents` skill and follow its artifact-start, design-preset, render, visual inspection, and accessibility requirements.
   - Use `compact_reference_guide` with a compact `editorial_cover` opening unless the user supplies another template.
   - Run `scripts/build_notes_docx.py --input notes.json --output output.docx` for deterministic authoring.
7. Verify and deliver.
   - Render every page and inspect it for clipping, broken glyphs, awkward page breaks, and dense mobile-unfriendly paragraphs.
   - Run heading, section, and accessibility audits where available.
   - Deliver only the final DOCX unless the user asks for transcripts or QA files.

## Quality rules

- Write short Chinese paragraphs with clear Heading 1/2/3 hierarchy.
- Keep the core conclusion and summary ahead of detailed notes.
- Use real Word lists; do not type fake bullets or manual numbering.
- Break full transcripts into readable paragraphs without changing meaning.
- Remove tracking parameters and secret-bearing query strings from displayed source links.
- Name the output `<video title>_笔记.docx` unless the user specifies otherwise.
- Save beside the video by default when the source is local.

## Example invocations

- `用 $video-to-word-notes 把 D:\课程\第15课.mp4 转成中文 Word 笔记。`
- `用 $video-to-word-notes 处理这个 B 站英文视频：中文翻译和笔记在前，最后附英文全文。`
- `用 $video-to-word-notes 把百度网盘里已经下载好的视频整理成 Word，不要逐句时间轴，只保留最后三段时间概览。`
