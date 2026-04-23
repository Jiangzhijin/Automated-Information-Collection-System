# 📑 项目索引

快速导航所有项目文件和文档。

## 🎯 入门指南

- **[快速开始指南](QUICKSTART.md)** - ⭐ 首先阅读这个
- **[项目完成总结](PROJECT_SUMMARY.md)** - 项目功能和架构总览
- **[完整项目文档](README.md)** - 详细的API文档和配置说明

## 🚀 启动应用

### Windows用户
```bash
# 一键启动
start.bat
```

### Linux/Mac用户
```bash
# 一键启动
bash start.sh
```

### 初次设置
```bash
# 自动安装依赖（推荐）
python init.py
```

## 📁 项目结构

```
backend/
├── app/
│   ├── app.py              # Flask API服务器
│   └── scheduler.py        # 定时任务调度器
├── scrapers/
│   └── news_scraper.py    # 新闻爬虫模块
├── data/                   # 新闻数据存储
├── config.py              # 配置文件
├── requirements.txt       # 依赖列表
└── run.py                 # 启动脚本

frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/        # React组件
│   ├── services/          # API服务
│   ├── App.jsx            # 主应用
│   └── index.jsx          # 入口文件
└── package.json           # 依赖配置

部署相关:
├── Dockerfile             # Docker配置
├── docker-compose.yml     # Docker Compose配置
├── DEPLOYMENT.md          # 部署指南
└── .gitignore             # Git忽略文件
```

## 🔧 常用命令

### 后端开发

```bash
# 安装依赖
cd backend && pip install -r requirements.txt

# 启动API服务
python app/app.py

# 启动定时任务
python app/scheduler.py

# 同时启动两者
python run.py

# 获取新闻
curl http://localhost:5000/api/news

# 刷新新闻
curl -X POST http://localhost:5000/api/news/refresh
```

### 前端开发

```bash
# 安装依赖
cd frontend && npm install

# 启动开发服务
npm start

# 构建生产版本
npm run build

# 访问前端
# http://localhost:3000
```

### Docker部署

```bash
# 启动所有服务
docker-compose up -d

# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```

## 📖 核心API端点

| 端点 | 方法 | 功能 |
|------|------|------|
| `/api/news` | GET | 获取新闻列表 |
| `/api/news/refresh` | POST | 刷新新闻 |
| `/api/stats` | GET | 获取统计信息 |
| `/api/health` | GET | 健康检查 |

## 🎨 前端功能

- ✅ 实时新闻展示
- ✅ 分页浏览
- ✅ 按源筛选
- ✅ 手动刷新
- ✅ 响应式设计
- ✅ 统计信息展示

## ⚙️ 后端功能

- ✅ BBC News爬虫
- ✅ Hacker News爬虫
- ✅ RSS源解析
- ✅ 定时自动获取
- ✅ JSON数据存储
- ✅ RESTful API
- ✅ CORS支持

## 📊 定时任务

```
每30分钟 → 自动获取新闻
  08:00 → 早晨更新
  12:00 → 中午更新
  18:00 → 下午更新
  22:00 → 晚上更新
```

## 🔍 故障排除

遇到问题？检查这些文件：

- **连接问题** → 查看[QUICKSTART.md#常见问题](QUICKSTART.md#常见问题)
- **部署问题** → 查看[DEPLOYMENT.md](DEPLOYMENT.md)
- **API问题** → 查看[README.md#-api文档](README.md#-api文档)
- **配置问题** → 编辑 `backend/config.py`

## 🚀 后续开发

### 添加新闻源

编辑 `backend/scrapers/news_scraper.py`：

```python
class MySource(NewsScraperBase):
    def parse_news(self):
        # 实现爬虫逻辑
        pass
```

### 自定义样式

编辑 `frontend/src/components/NewsList.css`

### 修改定时周期

编辑 `backend/app/scheduler.py` 中的 `start()` 方法

## 📚 文档导航

| 文档 | 内容 | 阅读时间 |
|------|------|---------|
| QUICKSTART.md | 5分钟快速上手 | 5分钟 |
| README.md | 完整文档和API文档 | 15分钟 |
| PROJECT_SUMMARY.md | 项目概览 | 10分钟 |
| DEPLOYMENT.md | 生产部署指南 | 20分钟 |

## 🎓 技术栈

**后端**
- Python 3.8+
- Flask - Web框架
- APScheduler - 定时任务
- feedparser - RSS解析
- requests - HTTP库
- BeautifulSoup - 网页解析

**前端**
- React 18
- Axios - HTTP客户端
- React Icons - 图标库
- CSS Grid/Flexbox - 布局

**部署**
- Docker & Docker Compose
- Gunicorn - Python WSGI服务器
- Nginx - 反向代理

## 📞 获取帮助

1. **查看日志**
   ```bash
   tail -f backend/data/scheduler.log
   ```

2. **检查API健康状态**
   ```bash
   curl http://localhost:5000/api/health
   ```

3. **浏览器控制台**
   - F12 打开开发者工具
   - Console 查看JavaScript错误

4. **查看错误消息**
   - 后端：控制台输出
   - 前端：浏览器Console

## ✨ 快速查询

### 我想要...

- **快速启动** → 运行 `start.bat` 或 `bash start.sh`
- **添加新闻源** → 编辑 `backend/scrapers/news_scraper.py`
- **修改外观** → 编辑 `frontend/src/components/NewsList.css`
- **改变更新频率** → 编辑 `backend/app/scheduler.py`
- **部署到服务器** → 查看 `DEPLOYMENT.md`
- **使用数据库** → 查看 `DEPLOYMENT.md` 的"数据库迁移"部分
- **查看API文档** → 查看 `README.md` 的"API文档"部分

## 🎯 下一步建议

1. **立即体验**
   - 运行启动脚本
   - 访问 http://localhost:3000

2. **理解架构**
   - 阅读 PROJECT_SUMMARY.md
   - 查看文件结构

3. **定制功能**
   - 添加新闻源
   - 修改样式
   - 调整定时周期

4. **部署上线**
   - 按照 DEPLOYMENT.md 部署
   - 配置域名和SSL

---

**现在就开始吧！** 🚀📰✨

**最后提醒：** 不要忘记在启动前运行 `python init.py` 来自动安装所有依赖！
