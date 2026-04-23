#!/usr/bin/env python3
"""
项目初始化脚本 - 自动安装依赖和创建必要目录
"""
import os
import sys
import subprocess
import platform

def print_header(text):
    """打印标题"""
    print("\n" + "=" * 50)
    print(f"  {text}")
    print("=" * 50)

def print_success(text):
    """打印成功信息"""
    print(f"✅ {text}")

def print_error(text):
    """打印错误信息"""
    print(f"❌ {text}")
    sys.exit(1)

def print_info(text):
    """打印信息"""
    print(f"ℹ️  {text}")

def check_python():
    """检查Python版本"""
    print_header("检查 Python")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print_error(f"Python版本过低，需要3.8+，当前版本：{version.major}.{version.minor}")
    
    print_success(f"Python版本：{version.major}.{version.minor}.{version.micro}")

def check_node():
    """检查Node.js"""
    print_header("检查 Node.js")
    
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        print_success(f"Node.js版本：{result.stdout.strip()}")
    except FileNotFoundError:
        print_error("Node.js未安装，请从 https://nodejs.org 下载安装")

def install_backend_deps():
    """安装后端依赖"""
    print_header("安装后端依赖")
    
    backend_dir = os.path.join(os.path.dirname(__file__), 'backend')
    requirements_file = os.path.join(backend_dir, 'requirements.txt')
    
    if not os.path.exists(requirements_file):
        print_error(f"找不到 requirements.txt：{requirements_file}")
    
    print_info("安装中...这可能需要几分钟")
    
    try:
        subprocess.run(
            [sys.executable, '-m', 'pip', 'install', '-r', requirements_file],
            cwd=backend_dir,
            check=True
        )
        print_success("后端依赖安装完成")
    except subprocess.CalledProcessError as e:
        print_error(f"后端依赖安装失败：{str(e)}")

def install_frontend_deps():
    """安装前端依赖"""
    print_header("安装前端依赖")
    
    frontend_dir = os.path.join(os.path.dirname(__file__), 'frontend')
    
    print_info("安装中...这可能需要几分钟")
    
    try:
        subprocess.run(
            ['npm', 'install'],
            cwd=frontend_dir,
            check=True
        )
        print_success("前端依赖安装完成")
    except subprocess.CalledProcessError as e:
        print_error(f"前端依赖安装失败：{str(e)}")

def create_data_dirs():
    """创建数据目录"""
    print_header("创建数据目录")
    
    data_dir = os.path.join(os.path.dirname(__file__), 'backend', 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    print_success(f"数据目录已创建：{data_dir}")

def show_next_steps():
    """显示下一步操作"""
    print_header("下一步")
    
    print("""
    初始化完成！现在你可以启动应用了。

    🚀 启动应用（选择一种方式）：

    方式1：一键启动（推荐）
    """)
    
    if platform.system() == 'Windows':
        print("       start.bat")
    else:
        print("       bash start.sh")
    
    print("""
    方式2：分步启动
       终端1：cd backend && python run.py
       终端2：cd frontend && npm start

    方式3：仅启动API
       cd backend
       python app/app.py

    📱 访问地址：
       - 前端: http://localhost:3000
       - 后端: http://localhost:5000/api/news
       - 文档: 查看 README.md 和 QUICKSTART.md

    💡 需要帮助？
       - 查看 QUICKSTART.md 快速开始指南
       - 查看 README.md 完整文档
       - 查看 PROJECT_SUMMARY.md 项目总结
    """)

def main():
    """主函数"""
    print_header("信息汇总网站 - 项目初始化")
    
    print("本脚本将自动安装所有依赖并配置项目")
    print("")
    
    # 检查环境
    check_python()
    check_node()
    
    # 创建目录
    create_data_dirs()
    
    # 安装依赖
    try:
        install_backend_deps()
    except Exception as e:
        print_error(f"后端依赖安装失败：{str(e)}")
    
    try:
        install_frontend_deps()
    except Exception as e:
        print_error(f"前端依赖安装失败：{str(e)}")
    
    # 显示完成信息
    print_header("初始化完成！")
    print_success("所有依赖已安装，项目已准备好启动")
    
    # 显示下一步
    show_next_steps()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  用户中止")
        sys.exit(0)
    except Exception as e:
        print_error(f"发生错误：{str(e)}")
