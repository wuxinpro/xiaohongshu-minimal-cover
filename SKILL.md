---
name: xiaohongshu-minimal-cover
description: "小红书极简扁平封面生成器。生成 3:4 竖版（1080×1440）封面图，白色圆角卡片 + 居中排版 + 机器人图标 + 自适应字号 + 关键词橙色高亮。"
---

# xiaohongshu-minimal-cover

小红书极简扁平封面生成器。根据用户提供的标题文案，自动分析关键词、自适应字号、选择机器人图标、生成标语，输出符合"6/16 极简扁平封面规范"的封面图。

## 设计规范

- **比例**: 3:4 竖版（宽 1080px × 高 1440px）
- **整体**: 白色圆角卡片独立作为封面，无外背景层
- **圆角**: 40px
- **投影**: 三层柔和阴影 + 1px 极细描边（`box-shadow: 0 4px 12px rgba(0,0,0,0.03), 0 16px 40px rgba(0,0,0,0.05), 0 32px 80px rgba(0,0,0,0.03), 0 0 0 1px rgba(0,0,0,0.02)`）
- **肌理**: 细腻颗粒感（SVG fractalNoise, opacity 0.035, baseFrequency 1.4, numOctaves 3）
- **卡片填充**: 60px 56px（上下/左右）
- **内容宽度**: 698px（预览 810px 卡片 / 全尺寸 968px 卡片）
- **图标**: 右上角 100px，橙色 #FF6B35，AI 科技主题机器人 SVG
- **标题第一行**: 居中，#1a1a1a，font-weight 800，自适应字号（max 100px / min 55px），white-space: nowrap，letter-spacing: 0px
- **标题第二行**: 居中，#1a1a1a，font-weight 700，字号 = 第一行 × 0.72，white-space: nowrap，letter-spacing: 1px
- **两行间距**: 20px gap
- **关键词**: 橙色 #FF6B35 高亮，每行最多 1-2 个，克制使用
- **分隔线**: 标题组与标语之间，60px 宽 × 2px 高，#D6D8DA，居中，margin-top: 12px
- **标语**: 靠右对齐，20px，#555555，font-weight 400，margin-right: 8px，align-self: flex-end
- **禁止**: NOT 9:16, NOT 机器人/动漫形象, NOT 暖白/米白背景, NOT 黑色边框, NOT 卡片嵌卡片, NOT 标题撑满, NOT 色号说明文字, NOT 蓝色标题, NOT OpenAI logo

## 触发条件

用户需要：
- 生成小红书封面
- 极简扁平风格封面
- 竖版 3:4 封面

## 工作流

1. **接收标题**: 用户提供封面文案
2. **智能拆行**: 使用 `split_title` 函数按最先出现的标点符号（！？。!?）拆为两行；无标点时按字符长度均分
3. **分析关键词**: 
   - 品牌词（GPT-5.6, ChatGPT, Capafy, 豆包 等）→ 橙色
   - 核心业务/产出词（代码, 打车, 技能, 发布 等）→ 橙色
   - 修饰/桥接词（突然, 进军, 秒变 等）→ 保留深炭黑
   - 每行不超过 2 个橙色点
4. **选择机器人图标**: 根据文案语义匹配
   - 新品/发布/变快/太香了 → 🤗 兴奋机器人
   - 教程/秒变/代码/步骤 → 🤔 思考机器人
   - 默认 → 🤖 标准机器人
5. **自适应字号**: `calc_adaptive_size` 函数计算一行能容纳的最大字号
6. **生成标语**: 如果用户未提供标语，根据关键词自动补充（代码→"无需提示词，一键复刻", 打车→"字节悄悄布局出行赛道" 等）
7. **生成预览 HTML**: 调用 `scripts/generate_cover.py` 输出预览文件
8. **用户确认后导出**: 根据确认结果输出最终 1080×1440 PNG

## 自适应字号算法

```python
CONTENT_WIDTH = 698  # 预览卡片内容宽度 810-56*2
MAX_LINE1_SIZE = 100
MIN_LINE1_SIZE = 55

def char_width_factor(ch):
    """计算单个字符的近似宽度系数"""
    if 中文字/全角标点: return 1.0
    if 空格: return 0.3
    if 连字符/点: return 0.3
    return 0.6  # 拉丁字母、数字

def calc_adaptive_size(text):
    total_factor = sum(char_width_factor(c) for c in text)
    max_size = int(CONTENT_WIDTH * 0.96 / total_factor)
    return max(MIN_LINE1_SIZE, min(MAX_LINE1_SIZE, max_size))
```

第二行字号 = max(36, int(第一行字号 × 0.72))

## 机器人 SVG 图标库

### 🤖 标准机器人（默认）
```svg
<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="4" y="6" width="16" height="13" rx="3" fill="#FF6B35"/>
  <rect x="1" y="9" width="3" height="7" rx="1.5" fill="#FF6B35" opacity="0.6"/>
  <rect x="20" y="9" width="3" height="7" rx="1.5" fill="#FF6B35" opacity="0.6"/>
  <line x1="12" y1="3" x2="12" y2="6" stroke="#FF6B35" stroke-width="2" stroke-linecap="round"/>
  <circle cx="12" cy="2.5" r="1.5" fill="#FF6B35"/>
  <circle cx="9" cy="11" r="2" fill="#ffffff"/>
  <circle cx="15" cy="11" r="2" fill="#ffffff"/>
  <circle cx="9" cy="11" r="0.8" fill="#FF6B35"/>
  <circle cx="15" cy="11" r="0.8" fill="#FF6B35"/>
  <path d="M9.5 15.5C10.5 16.5 13.5 16.5 14.5 15.5" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round"/>
</svg>
```

### 🤗 兴奋机器人（新品/新闻/惊喜）
```svg
<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="4" y="6" width="16" height="13" rx="3" fill="#FF6B35"/>
  <rect x="1" y="9" width="3" height="7" rx="1.5" fill="#FF6B35" opacity="0.6"/>
  <rect x="20" y="9" width="3" height="7" rx="1.5" fill="#FF6B35" opacity="0.6"/>
  <line x1="12" y1="3" x2="12" y2="6" stroke="#FF6B35" stroke-width="2" stroke-linecap="round"/>
  <circle cx="12" cy="2.5" r="1.5" fill="#FF6B35"/>
  <circle cx="9" cy="11" r="2" fill="#ffffff"/>
  <circle cx="15" cy="11" r="2" fill="#ffffff"/>
  <circle cx="9" cy="11" r="0.8" fill="#FF6B35"/>
  <circle cx="15" cy="11" r="0.8" fill="#FF6B35"/>
  <path d="M9 14.5L11 16.5L15 13.5" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="7" y1="6" x2="6" y2="4" stroke="#FF6B35" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="17" y1="6" x2="18" y2="4" stroke="#FF6B35" stroke-width="1.5" stroke-linecap="round"/>
</svg>
```

### 🤔 思考机器人（教程/技巧/代码）
```svg
<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="4" y="6" width="16" height="13" rx="3" fill="#FF6B35"/>
  <rect x="1" y="9" width="3" height="7" rx="1.5" fill="#FF6B35" opacity="0.6"/>
  <rect x="20" y="9" width="3" height="7" rx="1.5" fill="#FF6B35" opacity="0.6"/>
  <line x1="12" y1="3" x2="12" y2="6" stroke="#FF6B35" stroke-width="2" stroke-linecap="round"/>
  <circle cx="12" cy="2.5" r="1.5" fill="#FF6B35"/>
  <circle cx="9" cy="11" r="2" fill="#ffffff"/>
  <circle cx="15" cy="11" r="2" fill="#ffffff"/>
  <circle cx="9" cy="11" r="0.8" fill="#FF6B35"/>
  <circle cx="15" cy="11" r="0.8" fill="#FF6B35"/>
  <line x1="9.5" y1="16" x2="14.5" y2="16" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M10 15C10 16 11 16.5 12 16.5C13 16.5 14 16 14 15" stroke="#ffffff" stroke-width="1" stroke-linecap="round" fill="none"/>
</svg>
```


## 导出为 PNG

使用 \--export\ 参数自动输出 1080×1440 PNG：

\\\ash
python scripts/generate_cover.py --title "GPT-5.6 下周发布！截图秒变代码" --export images/cover.png
\\\

导出流程：
1. 生成 810×1080 HTML 预览
2. 自动缩放所有 px 值 × 4/3 → 1080×1440
3. 使用 Playwright 截图输出 PNG
4. 可直接用于小红书发布

> Playwright 会在首次运行时自动安装，如失败可手动截图预览页面。
## 输出

- `preview/*.html` — 浏览器可打开的预览文件（810×1080 缩放预览）
- `output/*.png` — 最终 1080×1440 封面图（需截图或 Playwright 导出）

## 小红书发布建议

- **app 标题**: 与封面内容一致，补充品牌词 + 行为词，搜索友好
- **封面以感叹号收尾**增加点击感
