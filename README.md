# video-to-word-notes

把本地视频或用户有权访问的在线视频，整理成忠实、清晰、适合手机阅读的 Word 笔记。

这个 Skill 先转写，再总结；对于英文视频，主要内容使用中文，并在文末保留完整的英文转写。正文不堆叠逐句时间戳，只在结尾提供三段时间概览。

## 它解决什么问题

普通的视频总结容易丢失姓名、数字、限定条件和例子，也很难直接成为可复习的文档。`video-to-word-notes` 把处理过程拆成可核对的步骤：

1. 解析本地文件或用户授权的视频来源。
2. 提取适合语音识别的单声道 16 kHz WAV。
3. 优先使用匹配音频的字幕，否则调用可用的 Whisper 或授权转写服务。
4. 在完整转写的基础上生成中文摘要、结构化笔记和行动清单。
5. 生成 DOCX，并检查分页、字体、标题层级和移动端可读性。

## 主要特性

- 支持本地 MP4、MOV、MKV、WebM 及常见音频文件。
- 可处理用户有权访问的 YouTube、Bilibili、好看视频或云盘来源。
- 中文视频生成中文笔记。
- 英文视频生成中文内容，并附完整英文转写。
- 保留姓名、数字、案例、否定词和说话者原意。
- 将不确定内容标记为 `[听不清]` 或 `[uncertain]`，不凭空补写。
- 清理展示链接中的 Token、签名及跟踪参数。
- 使用真实的 Word 标题与列表，而不是手工模拟格式。

## 安装

使用支持 Agent Skills 的安装工具：

```bash
npx skills add sunny19900911/video-to-word-notes
```

也可以克隆到 Codex 的 Skills 目录：

```bash
git clone https://github.com/sunny19900911/video-to-word-notes.git ~/.codex/skills/video-to-word-notes
```

重新开启一个 Codex 任务后即可使用。

## 使用示例

```text
用 $video-to-word-notes 把 D:\课程\第15课.mp4 转成中文 Word 笔记。
```

```text
用 $video-to-word-notes 处理这个 B 站英文视频：中文翻译和笔记在前，最后附英文全文。
```

```text
用 $video-to-word-notes 把已经下载好的网盘视频整理成 Word，不要逐句时间轴，只保留最后三段时间概览。
```

## 依赖与边界

- 音频提取需要 `ffmpeg`，也可以安装 `imageio-ffmpeg` 作为后备。
- DOCX 生成需要 `python-docx`。
- 转写引擎不随仓库分发；请使用本地 Whisper、已有字幕或你有权调用的转写服务。
- 登录受限或云盘内容应使用用户自己的授权会话，或先由用户下载到本地。
- 本项目不会绕过登录、验证码、付费墙、DRM 或平台访问控制。

示例安装：

```bash
pip install python-docx imageio-ffmpeg
```

## 仓库结构

| 路径 | 用途 |
| --- | --- |
| `SKILL.md` | Skill 的触发条件、完整工作流和质量规则 |
| `agents/openai.yaml` | Skill 在 Codex 界面中的名称与默认提示 |
| `scripts/extract_audio.py` | 从视频提取单声道 16 kHz PCM WAV |
| `scripts/build_notes_docx.py` | 根据结构化 JSON 生成 Word 笔记 |
| `references/source-and-transcription.md` | 来源解析、字幕与转写选择规则 |
| `references/notes-schema.md` | DOCX 构建脚本使用的 JSON 结构 |

## 隐私、版权与合理使用

- 只处理你拥有、购买、获准访问或依法可以处理的内容。
- 不要提交私人视频、Cookie、密码、Token、签名链接或完整转写到公开 Issue。
- 生成的笔记是对来源的整理，不代表可以重新分发受版权保护的视频或逐字稿。
- 使用云端模型或转写服务时，数据处理受相应服务商条款约束。

## 贡献与安全

欢迎修复转写流程、文档结构、跨平台兼容性和 DOCX 排版问题。提交前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

安全问题请不要创建公开 Issue，请按照 [SECURITY.md](SECURITY.md) 私下报告。

## License

本仓库的代码、Skill 定义和文档采用 [MIT License](LICENSE)。该许可证不授予任何第三方视频、字幕或转写内容的版权。
