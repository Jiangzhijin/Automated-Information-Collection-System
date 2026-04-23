@echo off
chcp 65001 >nul
echo ================================================
echo 🚀 信息汇总网站 - 启动脚本
echo ================================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python未安装或不在PATH中
    pause
    exit /b 1
)

echo ✅ Python版本检查完成

REM 进入backend目录
cd /d "%~dp0backend"

REM 检查依赖
echo 检查依赖...
python -c "import flask, feedparser, apscheduler" >nul 2>&1
if errorlevel 1 (
    echo ❌ 缺少依赖，请先运行：pip install -r requirements.txt
    pause
    exit /b 1
)

echo ✅ 依赖检查完成
echo.
echo 启动中...
echo - Flask API: http://localhost:5000
echo - React前端: http://localhost:3000 ^(需要单独运行 npm start^)
echo - 定时任务: 后台运行
echo.
echo 按 Ctrl+C 停止服务
echo.

REM 启动应用
python run.py

pause
