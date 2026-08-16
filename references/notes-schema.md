# Notes JSON schema

Pass a UTF-8 JSON object to `scripts/build_notes_docx.py`.

```json
{
  "title": "第15课 如何准确筛选对方的照片",
  "source": "本地视频文件名或清理后的网页地址",
  "language": "zh",
  "duration": "17分43秒",
  "one_sentence": "照片适合用于形成待验证的线索，不适合直接给人下结论。",
  "summary": [
    "先排除明显风险信号。",
    "再从照片组合判断对方主动展示的生活重点。"
  ],
  "sections": [
    {
      "heading": "常见误区",
      "paragraphs": ["不要只看外貌或财富展示。"],
      "bullets": ["忽视照片背后的情境", "因为单一标准过早否定"]
    }
  ],
  "checklist": ["反向搜图", "结合后续聊天和行为验证"],
  "translated_full_text": "英文视频时填写完整中文翻译；中文视频可省略。",
  "time_ranges": [
    {"range": "00:00-05:00", "summary": "第一部分"},
    {"range": "05:00-10:00", "summary": "第二部分"},
    {"range": "10:00-15:00", "summary": "第三部分"}
  ],
  "english_transcript": "English videos must include the complete cleaned transcript here."
}
```

## Required fields

- `title`
- `one_sentence`
- `summary`: non-empty string array
- `sections`: non-empty array
- `time_ranges`: exactly three entries

## Conditional fields

- Set `translated_full_text` for English videos when a full Chinese translation is needed.
- Set `english_transcript` for every English video. The builder rejects `language: "en"` when this field is empty.

## Section fields

Each section needs `heading` and at least one of `paragraphs` or `bullets`. Use multiple sections rather than long paragraphs. Keep the schema content in Chinese except for the English appendix and necessary original terms.
