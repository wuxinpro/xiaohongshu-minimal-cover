#!/usr/bin/env python3
"""generate_cover.py — 小红书极简扁平封面生成器

根据标题文案自动分析关键词、自适应字号、选择合适的图标，
生成符合"6/16 极简扁平封面规范"的 HTML 预览。

用法:
  python generate_cover.py --line1 "GPT-5.6" --line2 "截图秒变代码" --slogan "无需提示词，一键复刻"
  python generate_cover.py --title "ChatGPT突然变快了？新功能实测太香了！" --slogan "不用等待思考过程，秒回常见问题"

参数:
  --title    完整标题（自动拆分为两行，优先使用）
  --line1    第一行文本（如已拆分，与 --line2 配合使用）
  --line2    第二行文本
  --slogan   标语（可选，自动生成）
  --app-title 小红书发布标题（可选）
  --output   输出路径（可选）
"""

import argparse
import math
import os
import re
import sys
# Template not needed — using manual replace

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'cover_template.html')

# === 自适应字号计算 ===
CONTENT_WIDTH = 698  # 预览卡片内容宽度 810-56*2（px）
MAX_LINE1_SIZE = 100
MIN_LINE1_SIZE = 55

def char_width_factor(ch):
    """计算单个字符的近似宽度系数"""
    if '\u4e00' <= ch <= '\u9fff' or '\u3000' <= ch <= '\u303f' or '\uff00' <= ch <= '\uffef':
        return 1.0  # 中文 + 全角标点
    if ch in ' 　':
        return 0.3  # 空格
    if ch in '-.':
        return 0.3  # 连字符、点
    return 0.6  # 拉丁字母、数字

def calc_text_width(text, font_size):
    """估算文本在给定字号下的像素宽度"""
    total = sum(char_width_factor(c) for c in text)
    return total * font_size

def calc_adaptive_size(text):
    """计算第一行自适应字号"""
    total_factor = sum(char_width_factor(c) for c in text)
    if total_factor == 0:
        return MAX_LINE1_SIZE
    max_size = int(CONTENT_WIDTH * 0.96 / total_factor)
    return max(MIN_LINE1_SIZE, min(MAX_LINE1_SIZE, max_size))

# === 关键词分析 ===
BRAND_KEYWORDS = [
    'chatgpt', 'gpt', 'capafy', '豆包', 'openai', 'google', 'meta',
    'apple', '微软', '字节', '百度', '阿里', '腾讯',
]

FEATURE_KEYWORDS = [
    '代码', '打车', '测试', '发布', '功能', '技能',
    '市场', '平台', '产品', '模型',
]

def analyze_keywords(line1, line2):
    """分析并标记两行中的关键词，返回 HTML"""
    def highlight(text, brand_words, feature_words):
        result = []
        i = 0
        while i < len(text):
            matched = False
            for word in sorted(brand_words + feature_words, key=len, reverse=True):
                if text[i:i+len(word)] == word:
                    # Check word boundaries for Latin words
                    result.append(f'<span class="kw">{word}</span>')
                    i += len(word)
                    matched = True
                    break
            if not matched:
                result.append(text[i])
                i += 1
        return ''.join(result)
    
    # Build word list from the text
    brand_hits = []
    feature_hits = []
    for kw in BRAND_KEYWORDS:
        if kw.lower() in line1.lower() or kw.lower() in line2.lower():
            # Find the exact case instance
            for txt in [line1, line2]:
                idx = txt.lower().find(kw.lower())
                if idx >= 0:
                    brand_hits.append(txt[idx:idx+len(kw)])
    for kw in FEATURE_KEYWORDS:
        if kw in line1 or kw in line2:
            feature_hits.append(kw)
    
    # Only highlight at most 2 keywords per line
    line1_html = highlight(line1, brand_hits[:2], feature_hits[:2])
    line2_html = highlight(line2, brand_hits[:2], feature_hits[:2])
    
    return line1_html, line2_html

# === 图标选择 ===
# AI 科技主题 — 统一使用机器人小图标
# 简洁圆角机器人头像，扁平风格，橙色 #FF6B35
# 根据文案类别选择不同的机器人表情/姿势

# 默认机器人（AI 科技通用）
ICON_ROBOT = '''<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
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
      </svg>'''

# 机器人 + 惊喜/兴奋表情（新品发布、新闻）
ICON_ROBOT_EXCITED = '''<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
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
      </svg>'''

# 机器人 + 学习/思考（教程技巧）
ICON_ROBOT_THINK = '''<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
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
      </svg>'''


def select_icon(line1, line2, slogan):
    """根据文案语义选择对应的机器人图标"""
    text = (line1 + ' ' + line2 + ' ' + slogan)

    # 科技新品 / 发布 → 兴奋机器人
    if any(kw in text for kw in ['发布', '首发', '上线', '新品', '升级', '变快', '速度', '太香了']):
        return ICON_ROBOT_EXCITED

    # 教程 / 技巧 / 学习 → 思考机器人
    if any(kw in text for kw in ['教程', '技巧', '秒变', '攻略', '教学', '指南', '怎么', '如何', '步骤', '代码']):
        return ICON_ROBOT_THINK

    # 行业新闻 / 布局
    if any(kw in text for kw in ['布局', '赛道', '市场', '行业', '进军', '全球']):
        return ICON_ROBOT_EXCITED

    # 默认: 标准机器人
    return ICON_ROBOT


def icon_name(icon):
    """返回图标中文名称"""
    names = {
        id(ICON_ROBOT): '机器人', id(ICON_ROBOT_EXCITED): '机器人-兴奋',
        id(ICON_ROBOT_THINK): '机器人-思考',
    }
    return names.get(id(icon), '机器人')

# === 标语生成 ===
def generate_slogan(line1, line2):
    """根据标题自动生成标语"""
    # Simple heuristic-based slogan generation
    text = line1 + line2
    slogans = {
        '代码': '无需提示词，一键复刻',
        '打车': '字节悄悄布局出行赛道',
        '变快': '不用等待思考过程，秒回常见问题',
        '技能': '全球首个 AI 技能市场',
        '发布': '最新版本抢先体验',
    }
    for keyword, slogan in slogans.items():
        if keyword in text:
            return slogan
    return '最新动态抢先看'

# === 主逻辑 ===
def split_title(title):
    """将完整标题按最先出现的标点符号拆分为两行"""
    # Find the earliest occurring separator
    best_sep = None
    best_pos = len(title)
    for sep in ['！', '？', '。', '!', '?']:
        pos = title.find(sep)
        if 0 < pos < best_pos:
            best_pos = pos
            best_sep = sep
    if best_sep and best_pos >= 3:
        return title[:best_pos+1], title[best_pos+1:].strip()
    # Try half split
    mid = len(title) // 2
    return title[:mid], title[mid:]


def render(line1, line2, slogan='', icon_svg=None, title=None):
    """填充模板生成 HTML"""
    if not os.path.exists(TEMPLATE_PATH):
        sys.exit(f'错误: 找不到模板文件 {TEMPLATE_PATH}')

    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()

    if not title:
        title = f'{line1} {line2}'

    # Adaptive sizing
    line1_size = calc_adaptive_size(line1)
    line2_size = max(36, int(line1_size * 0.72))

    # Keyword analysis
    line1_html, line2_html = analyze_keywords(line1, line2)

    # Icon
    if not icon_svg:
        icon_svg = select_icon(line1, line2, slogan)

    mapping = {
        'TITLE': title,
        'LINE1_SIZE': str(line1_size),
        'LINE2_SIZE': str(line2_size),
        'LINE1_HTML': line1_html,
        'LINE2_HTML': line2_html,
        'ICON_SVG': icon_svg,
        'SLOGAN_TEXT': slogan,
    }

    html = template
    for key, value in mapping.items():
        html = html.replace('{{' + key + '}}', str(value))
    return html


def main():
    parser = argparse.ArgumentParser(description='生成小红书极简扁平封面')
    parser.add_argument('--title', default=None, help='完整标题（自动拆行）')
    parser.add_argument('--line1', default=None, help='第一行')
    parser.add_argument('--line2', default=None, help='第二行')
    parser.add_argument('--slogan', default=None, help='标语（可选）')
    parser.add_argument('--app-title', default=None, help='小红书发布标题')
    parser.add_argument('--output', default=None, help='输出路径')

    args = parser.parse_args()

    # Determine line1 and line2
    if args.title:
        if args.line1 or args.line2:
            print('提示: --title 和 --line1/--line2 同时提供，优先使用 --title 进行拆分')
        line1, line2 = split_title(args.title)
    elif args.line1 and args.line2:
        line1, line2 = args.line1, args.line2
    else:
        parser.print_help()
        sys.exit('错误: 需要提供 --title 或 --line1 + --line2')

    # Slogan
    slogan = args.slogan if args.slogan else generate_slogan(line1, line2)

    # Render
    html = render(line1=line1, line2=line2, slogan=slogan, title=args.title)

    # Output path
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'preview')
    output_path = args.output or os.path.join(output_dir, 'xiaohongshu-minimal-cover.html')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    abs_path = os.path.abspath(output_path)
    line1_size = calc_adaptive_size(line1)
    print(f'✅ 封面已生成: {abs_path}')
    print(f'   字号: 第1行 {line1_size}px / 第2行 {max(36, int(line1_size * 0.72))}px')
    print(f'   图标: 🤖 {icon_name(select_icon(line1, line2, slogan))}')
    print(f'   在浏览器中打开即可预览')
    print()
    if args.app_title:
        print(f'📱 小红书发布标题: {args.app_title}')
    else:
        print(f'📱 小红书发布标题建议: {line1} {line2}')


if __name__ == '__main__':
    main()
