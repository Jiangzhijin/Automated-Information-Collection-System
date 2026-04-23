FROM python:3.9-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 安装Node.js（用于前端）
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs

# 复制后端依赖
COPY backend/requirements.txt ./backend/

# 安装Python依赖
RUN pip install --no-cache-dir -r backend/requirements.txt

# 复制前端依赖
COPY frontend/package.json frontend/package-lock.json ./frontend/

# 安装前端依赖
RUN cd frontend && npm install --production

# 复制应用代码
COPY backend ./backend
COPY frontend ./frontend

# 暴露端口
EXPOSE 5000 3000

# 启动脚本
CMD ["python", "backend/run.py"]
