# 🤖 小红书极简扁平封面生成器 (xiaohongshu-minimal-cover)

自动生成符合「6/16 极简扁平封面规范」的小红书 3:4 竖版封面图。

## 效果预览

| GPT-5.6 下周发布 | 豆包 AI 打车 | ChatGPT 实测 |
|---------|---------|---------|
| ![GPT-5.6](images/demo-gpt56.png) | ![豆包](images/demo-doubao.png) | ![ChatGPT](images/demo-chatgpt.png) |

## 安装到 Codex

```bash
npx skills add wuxinpro/xiaohongshu-minimal-cover
```

## 快速使用

```bash
# 生成预览 + 导出 1080×1440 PNG（推荐）
python scripts/generate_cover.py --title "GPT-5.6 下周发布！截图秒变代码" --export cover.png

# 仅生成 HTML 预览
python scripts/generate_cover.py --title "GPT-5.6 下周发布！截图秒变代码"

# 自定义两行 + 标语
python scripts/generate_cover.py --line1 "豆包 AI 能打车了！" --line2 "一句话叫车" --slogan "字节悄悄布局出行赛道"
```

## 参数

| 参数 | 说明 |
|------|------|
| `--title` | 完整标题，自动拆为两行 |
| `--line1` / `--line2` | 手动指定两行 |
| `--slogan` | 标语（自动生成） |
| `--export` | 导出为 1080×1440 PNG（需 Playwright，自动安装） |
| `--app-title` | 小红书发布标题 |
| `--output` | 预览 HTML 输出路径 |

## 设计规范

- **比例**: 3:4 竖版（1080×1440），白色圆角卡片独立作为封面
- **标题**: 两行居中，深炭黑 #1a1a1a，字号自适应不折行
- **关键词**: #FF6B35 橙色高亮
- **图标**: 右上角机器人 SVG（3 种表情按文案匹配）
- **标语**: 靠右对齐 20px #555

## 自适应导出流程

1. 脚本生成 810×1080 HTML 预览
2. 使用 `--export` 时自动缩放所有 px 值 × 4/3
3. Playwright 截图输出 1080×1440 PNG
4. 可直接用于小红书发布
