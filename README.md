# 📰 信息汇总网站

一个实时新闻聚合平台，支持定时获取BBC News等多个新闻源的最新资讯。

## 🌟 功能特性

- ✅ **定时自动获取新闻** - 支持RSS源和网页爬虫
- ✅ **多新闻源聚合** - BBC News、Hacker News等
- ✅ **实时数据更新** - 每30分钟自动更新，支持特定时间更新
- ✅ **RESTful API** - 提供灵活的数据接口
- ✅ **React前端界面** - 现代化、响应式的用户界面
- ✅ **分页浏览** - 支持按来源筛选和分页查看
- ✅ **文件存储** - 无需数据库，新闻保存为JSON文件

## 📋 项目结构

```
信息处理/
├── backend/
│   ├── app/
│   │   ├── app.py              # Flask主应用
│   │   ├── scheduler.py        # 定时任务调度器
│   │   └── __init__.py
│   ├── scrapers/
│   │   ├── news_scraper.py    # 爬虫模块（RSS + 网页爬虫）
│   │   └── __init__.py
│   ├── data/                   # 存储新闻数据的目录
│   │   ├── all_news.json      # 所有新闻数据
│   │   ├── articles.json      # 文章列表
│   │   └── scheduler.log      # 定时任务日志
│   ├── config.py              # 配置文件
│   ├── requirements.txt        # Python依赖
│   └── run.py                 # 启动脚本
│
├── frontend/
│   ├── public/
│   │   └── index.html         # HTML入口
│   ├── src/
│   │   ├── components/
│   │   │   ├── NewsList.jsx   # 新闻列表组件
│   │   │   └── NewsList.css   # 组件样式
│   │   ├── services/
│   │   │   └── api.js         # API服务
│   │   ├── App.jsx            # 应用主组件
│   │   ├── App.css            # 应用样式
│   │   └── index.jsx          # 入口文件
│   └── package.json           # NPM依赖
│
└── README.md                  # 项目说明文档
```

## 🚀 快速开始

### 系统要求
- Python 3.8+
- Node.js 14+
- npm 或 yarn

### 后端设置

#### 1. 安装Python依赖
```bash
cd backend
pip install -r requirements.txt
```

#### 2. 运行Flask应用
```bash
# 方式一：直接运行
python app/app.py

# 方式二：使用启动脚本（如果有）
python run.py
```

Flask服务将在 `http://localhost:5000` 启动

#### 3. 启动定时任务（可选）
在另一个终端运行：
```bash
python app/scheduler.py
```

这将启动定时新闻获取任务：
- 每30分钟自动获取一次新闻
- 每天 08:00, 12:00, 18:00, 22:00 自动更新

### 前端设置

#### 1. 安装npm依赖
```bash
cd frontend
npm install
```

#### 2. 启动开发服务器
```bash
npm start
```

React应用将在 `http://localhost:3000` 启动

## 📖 API文档

### 获取新闻列表
```
GET /api/news?page=1&per_page=20&source=BBC
```

**参数：**
- `page` (可选): 页码，默认为1
- `per_page` (可选): 每页条数，默认为20
- `source` (可选): 按新闻源筛选

**响应示例：**
```json
{
  "status": "success",
  "data": [
    {
      "title": "新闻标题",
      "link": "https://example.com",
      "description": "新闻摘要",
      "source": "BBC News - world",
      "published": "2024-04-23T10:30:00",
      "timestamp": "2024-04-23T12:00:00"
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 500,
    "pages": 25
  }
}
```

### 手动刷新新闻
```
POST /api/news/refresh
```

**响应示例：**
```json
{
  "status": "success",
  "message": "成功获取 150 条新闻",
  "total": 150,
  "timestamp": "2024-04-23T12:00:00"
}
```

### 获取统计信息
```
GET /api/stats
```

**响应示例：**
```json
{
  "status": "success",
  "total_articles": 500,
  "sources": ["BBC News - world", "BBC News - business", "Hacker News"],
  "sources_count": {
    "BBC News - world": 150,
    "BBC News - business": 120,
    "Hacker News": 230
  },
  "last_update": "2024-04-23T12:00:00"
}
```

### 健康检查
```
GET /api/health
```

## 🛠️ 配置说明

### 后端配置 (backend/config.py)

```python
SCRAPER_TIMEOUT = 10      # 爬虫超时时间（秒）
SCRAPER_RETRY = 3         # 爬虫重试次数
SCHEDULER_INTERVAL = 30   # 定时任务间隔（分钟）
SCHEDULER_ENABLED = True  # 是否启用定时任务
```

### 新增新闻源

编辑 `backend/scrapers/news_scraper.py`，在 `NewsAggregator` 类中添加新的爬虫：

```python
class MyNewsScraper(NewsScraperBase):
    def __init__(self):
        super().__init__()
        self.rss_url = 'https://example.com/rss'
    
    def parse_news(self):
        scraper = RSSNewsScraper(self.rss_url, 'My News Source')
        return scraper.parse_news()

# 在NewsAggregator中添加
self.scrapers = [
    BBCNewsScraper(),
    NewsAPIScraperNewsCom(),
    MyNewsScraper(),  # 新增
]
```

## 📊 数据存储

所有新闻数据存储在 `backend/data/` 目录中：

- **all_news.json** - 所有聚合的新闻数据
- **articles.json** - 新闻文章列表
- **scheduler.log** - 定时任务执行日志

## 🔧 故障排除

### 问题：前端无法连接到后端
- 确保Flask服务在 `http://localhost:5000` 运行
- 检查CORS设置是否正确启用
- 查看浏览器控制台的错误信息

### 问题：爬虫获取失败
- 检查网络连接
- 验证RSS源URL是否有效
- 查看 `scheduler.log` 文件获取错误详情

### 问题：定时任务不执行
- 确保 `scheduler.py` 脚本在运行
- 检查系统时间是否正确
- 查看控制台输出的任务执行日志

## 🚀 生产部署

### 使用Gunicorn部署Flask应用

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### 使用PM2管理定时任务

```bash
npm install -g pm2
pm2 start app/scheduler.py --name news-scheduler
pm2 save
pm2 startup
```

## 📝 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📞 联系方式

如有问题，请提交Issue或联系开发者。

---

**祝你使用愉快！** 📰✨
