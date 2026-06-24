#!/bin/bash
# xiaohongshu-minimal-cover — one-line install for Claude Code
# Usage: curl -fsSL https://raw.githubusercontent.com/wuxinpro/xiaohongshu-minimal-cover/main/install.sh | bash

set -e
SKILL_DIR="$HOME/.claude/skills/xiaohongshu-minimal-cover"
REPO_URL="https://github.com/wuxinpro/xiaohongshu-minimal-cover.git"

if [ -d "$SKILL_DIR" ]; then
  echo "==> Updating existing install at $SKILL_DIR ..."
  cd "$SKILL_DIR" && git pull
else
  echo "==> Installing xiaohongshu-minimal-cover to $SKILL_DIR ..."
  git clone --depth 1 "$REPO_URL" "$SKILL_DIR"
fi

echo ""
echo "✅ xiaohongshu-minimal-cover installed!"
echo "   Try: '帮我用 xiaohongshu-minimal-cover 做一组小红书配图'"
