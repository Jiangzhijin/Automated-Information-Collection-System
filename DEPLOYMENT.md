# 🚀 部署指南

本指南将帮助你将信息汇总网站部署到生产环境。

## 📋 部署选项

### 1. Docker部署（推荐）

#### 前置条件
- 安装 Docker 和 Docker Compose
- 足够的系统资源

#### 快速部署

```bash
# 一键启动所有服务
docker-compose up -d

# 查看服务状态
docker-compose ps

# 查看服务日志
docker-compose logs -f

# 停止服务
docker-compose down
```

#### 访问地址
- 前端: http://localhost:3000
- 后端API: http://localhost:5000/api

### 2. 云平台部署

#### Heroku部署

1. **安装Heroku CLI**
```bash
# macOS
brew tap heroku/brew && brew install heroku

# Windows
choco install heroku-cli
```

2. **创建Procfile**
```
web: cd backend && gunicorn -w 4 app:app
worker: cd backend && python app/scheduler.py
```

3. **部署**
```bash
heroku login
heroku create your-app-name
git push heroku main
```

#### AWS EC2部署

1. **创建EC2实例**（Ubuntu 20.04）

2. **安装依赖**
```bash
sudo apt-get update
sudo apt-get install -y python3-pip nodejs npm nginx

# 克隆项目
git clone your-repo.git
cd your-project
```

3. **配置Gunicorn**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 --chdir backend app:app
```

4. **配置Nginx反向代理**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:3000;
    }

    location /api/ {
        proxy_pass http://localhost:5000;
    }
}
```

5. **配置SSL（Let's Encrypt）**
```bash
sudo apt-get install -y certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

### 3. 虚拟主机/VPS部署

#### 使用PM2管理进程

1. **安装PM2**
```bash
npm install -g pm2
```

2. **创建ecosystem.config.js**
```javascript
module.exports = {
  apps: [
    {
      name: 'news-api',
      script: './backend/app/app.py',
      interpreter: 'python3',
      instances: 2,
      exec_mode: 'cluster',
    },
    {
      name: 'news-scheduler',
      script: './backend/app/scheduler.py',
      interpreter: 'python3',
    },
    {
      name: 'news-frontend',
      script: 'npm',
      args: 'start',
      cwd: './frontend',
    }
  ]
};
```

3. **启动应用**
```bash
pm2 start ecosystem.config.js
pm2 save
pm2 startup
```

## 🔒 生产环境配置

### 环境变量设置

创建 `.env` 文件：
```bash
# Flask配置
FLASK_ENV=production
FLASK_DEBUG=0
SECRET_KEY=your-secret-key-here

# 爬虫配置
SCRAPER_TIMEOUT=15
SCRAPER_RETRY=3

# 定时任务配置
SCHEDULER_INTERVAL=60
SCHEDULER_ENABLED=1
```

### 数据库迁移

如果想使用数据库而不是文件存储：

1. **安装SQLAlchemy**
```bash
pip install flask-sqlalchemy psycopg2-binary
```

2. **创建数据库模型**（在backend中）
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    link = db.Column(db.String(500))
    source = db.Column(db.String(100))
    published = db.Column(db.DateTime)
```

3. **迁移脚本**
```bash
flask db init
flask db migrate
flask db upgrade
```

## 📊 监控和维护

### 日志管理

```bash
# 查看Flask日志
tail -f backend/data/scheduler.log

# 使用systemd日志
journalctl -u news-aggregator -f
```

### 备份数据

```bash
# 备份JSON文件
tar -czf news-backup-$(date +%Y%m%d).tar.gz backend/data/

# 定期备份（cron）
0 2 * * * tar -czf /backups/news-$(date +\%Y\%m\%d).tar.gz /app/backend/data/
```

### 性能优化

1. **启用缓存**
```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/api/news')
@cache.cached(timeout=300)
def get_news():
    # ...
```

2. **使用CDN**
```nginx
location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
    expires 365d;
    add_header Cache-Control "public, immutable";
}
```

3. **启用Gzip压缩**
```nginx
gzip on;
gzip_types text/plain text/css application/json application/javascript;
```

## 🚨 故障排查

### 常见问题

**1. 数据库连接失败**
```bash
# 检查数据库服务
systemctl status postgresql

# 检查连接字符串
echo $DATABASE_URL
```

**2. 内存不足**
```bash
# 查看内存使用
free -h

# 扩展虚拟内存
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

**3. 定时任务不执行**
```bash
# 检查时区设置
timedatectl

# 查看APScheduler日志
tail -f backend/data/scheduler.log
```

## 📈 扩展建议

### 高可用部署

```yaml
# 使用Kubernetes
apiVersion: apps/v1
kind: Deployment
metadata:
  name: news-aggregator
spec:
  replicas: 3
  selector:
    matchLabels:
      app: news-aggregator
  template:
    metadata:
      labels:
        app: news-aggregator
    spec:
      containers:
      - name: backend
        image: your-registry/news-aggregator:latest
        ports:
        - containerPort: 5000
```

### 数据库优化

- 添加索引：`CREATE INDEX idx_source ON articles(source);`
- 定期清理旧数据：`DELETE FROM articles WHERE published < NOW() - INTERVAL '30 days';`
- 使用只读副本进行查询

### 消息队列

使用Redis或RabbitMQ处理异步任务：

```python
from celery import Celery

celery = Celery(app.name)

@celery.task
def fetch_news_task():
    aggregator.save_news()
```

## 📞 支持资源

- Docker文档: https://docs.docker.com
- Heroku部署: https://devcenter.heroku.com
- Nginx文档: https://nginx.org/en/docs/
- Flask部署: https://flask.palletsprojects.com/deployment/

---

**祝部署顺利！** 🎉
