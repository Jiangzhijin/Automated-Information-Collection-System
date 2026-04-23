#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
快速启动脚本 - 信息汇总网站
同时启动后端和前端
"""

import subprocess
import time
import os
import sys
import threading

def run_backend():
    """启动 Flask 后端"""
    print("[后端] 启动 Flask 服务器...")
    try:
        os.chdir(os.path.join(os.path.dirname(__file__), 'backend'))
        subprocess.run([sys.executable, 'app/app.py'], check=True)
    except KeyboardInterrupt:
        print("\n[后端] 已停止")
    except Exception as e:
        print(f"[后端] 错误: {e}")

def run_frontend():
    """启动 React 前端"""
    print("[前端] 等待3秒后启动 React 服务器...")
    time.sleep(3)
    
    print("[前端] 启动 React 服务器...")
    try:
        os.chdir(os.path.join(os.path.dirname(__file__), 'frontend'))
        # 设置环境变量
        env = os.environ.copy()
        env['DANGEROUSLY_DISABLE_HOST_CHECK'] = 'true'
        subprocess.run([os.path.join(os.path.dirname(os.sys.executable), 'npm'), 'start'], 
                      env=env, check=True)
    except KeyboardInterrupt:
        print("\n[前端] 已停止")
    except Exception as e:
        print(f"[前端] 错误: {e}")

def main():
    print("="*60)
    print("信息汇总网站 - 快速启动")
    print("="*60)
    print()
    
    # 在后台线程启动前端
    frontend_thread = threading.Thread(target=run_frontend, daemon=True)
    frontend_thread.start()
    
    # 在主线程启动后端
    try:
        run_backend()
    except KeyboardInterrupt:
        print("\n正在关闭所有服务...")
        sys.exit(0)

if __name__ == '__main__':
    main()
