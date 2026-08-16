# Contributing to video-to-word-notes

感谢你帮助改进 `video-to-word-notes`。我们欢迎能提升转写忠实度、Word 可读性、跨平台兼容性或文档清晰度的贡献。

## 基本原则

- 一次 Pull Request 只解决一个明确问题。
- 行为变化必须附带可复现的输入、测试或前后对比。
- 保持 `SKILL.md` 精简；优先修改现有规则，避免重复说明。
- 不上传受版权保护的视频、完整字幕、私人录音或真实访问凭据。
- 不加入绕过登录、验证码、DRM、付费墙或其他访问控制的实现。
- 不确定的转写应明确标记，不要用猜测填补原文。

## 本地准备

```bash
git clone https://github.com/sunny19900911/video-to-word-notes.git
cd video-to-word-notes
python -m venv .venv
```

激活虚拟环境后安装运行依赖：

```bash
pip install python-docx imageio-ffmpeg
```

系统也可以直接提供 `ffmpeg`。转写测试请自行配置本地 Whisper 或使用不包含隐私内容的测试字幕。

## 提交前检查

```bash
python -m py_compile scripts/extract_audio.py scripts/build_notes_docx.py
python /path/to/skill-creator/scripts/quick_validate.py .
```

如修改 `build_notes_docx.py`，还应使用最小示例 JSON 生成 DOCX，渲染并检查：

- 标题层级与真实列表是否正确；
- 中文字体是否正常；
- 是否存在裁切、孤行或异常分页；
- 英文视频是否包含完整英文附录；
- 时间概览是否恰好为三段。

## Pull Request

- 标题简洁说明结果，例如 `fix: preserve source numbers in notes`。
- 描述问题、解决方式、验证方法和已知限制。
- 行为修改应同步更新相关文档或示例。
- 不要混入格式化、重命名或其他无关重构。
- 确保仓库中没有视频、音频、生成的 DOCX、缓存目录、密钥或签名 URL。

## 报告问题

普通 Bug 可以创建公开 Issue，并提供：

- 操作系统、Python 与 ffmpeg 版本；
- 输入格式和大致时长；
- 使用字幕还是语音识别；
- 完整但已脱敏的错误信息；
- 能公开分享的最小复现材料。

涉及漏洞、隐私泄露或访问控制的问题，请遵循 [SECURITY.md](SECURITY.md)，不要公开披露。
