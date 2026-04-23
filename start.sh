#!/bin/bash

echo "================================================"
echo "🚀 信息汇总网站 - 启动脚本"
echo "================================================"
echo ""

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3未安装"
    exit 1
fi

echo "✅ Python版本检查完成"

# 进入backend目录
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/backend"

# 检查依赖
echo "检查依赖..."
python3 -c "import flask, feedparser, apscheduler" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ 缺少依赖，请先运行：pip install -r requirements.txt"
    exit 1
fi

echo "✅ 依赖检查完成"
echo ""
echo "启动中..."
echo "- Flask API: http://localhost:5000"
echo "- React前端: http://localhost:3000 (需要单独运行 npm start)"
echo "- 定时任务: 后台运行"
echo ""
echo "按 Ctrl+C 停止服务"
echo ""

# 启动应用
python3 run.py

trap "echo ''; echo '✅ 服务已停止'; exit 0" SIGINT
