#!/usr/bin/env python3
"""
一键启动脚本 - 同时启动Flask后端和定时任务
"""
import os
import sys
import subprocess
import time
from threading import Thread

def run_flask():
    """运行Flask应用"""
    os.chdir(os.path.join(os.path.dirname(__file__), 'backend'))
    subprocess.run([sys.executable, 'app/app.py'])

def run_scheduler():
    """运行定时任务"""
    time.sleep(2)  # 等待Flask启动
    os.chdir(os.path.join(os.path.dirname(__file__), 'backend'))
    subprocess.run([sys.executable, 'app/scheduler.py'])

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 信息汇总网站 - 启动脚本")
    print("=" * 50)
    
    # 检查依赖
    try:
        import flask
        import feedparser
        import apscheduler
    except ImportError:
        print("❌ 缺少依赖，请先运行：pip install -r backend/requirements.txt")
        sys.exit(1)
    
    print("✅ 依赖检查完成")
    print("\n启动中...")
    print("- Flask API: http://localhost:5000")
    print("- React前端: http://localhost:3000 (需要单独运行 npm start)")
    print("- 定时任务: 后台运行")
    print("\n按 Ctrl+C 停止服务\n")
    
    # 创建线程
    flask_thread = Thread(target=run_flask, daemon=False)
    scheduler_thread = Thread(target=run_scheduler, daemon=True)
    
    # 启动线程
    flask_thread.start()
    scheduler_thread.start()
    
    try:
        flask_thread.join()
    except KeyboardInterrupt:
        print("\n\n✋ 停止服务...")
        print("✅ 服务已停止")
