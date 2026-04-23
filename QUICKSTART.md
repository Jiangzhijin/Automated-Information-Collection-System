# 快速开始指南

## 📦 安装步骤

### 第一步：安装后端依赖

```bash
# Windows
cd backend
pip install -r requirements.txt

# Linux/Mac
cd backend
pip3 install -r requirements.txt
```

### 第二步：启动后端服务

**选项1：一键启动（推荐）**
```bash
# Windows
start.bat

# Linux/Mac
bash start.sh
```

**选项2：分别启动**

方式1 - 仅运行Flask API：
```bash
cd backend
python app/app.py
```

方式2 - 同时运行Flask和定时任务：
```bash
cd backend
python run.py
```

### 第三步：启动前端服务

在新的终端窗口中运行：

```bash
cd frontend
npm install          # 首次运行需要安装依赖
npm start
```

## ✅ 验证服务是否正常

打开浏览器访问以下地址：

- 🌐 **前端应用**: http://localhost:3000
- 🔌 **后端健康检查**: http://localhost:5000/api/health
- 📊 **新闻API**: http://localhost:5000/api/news
- 📈 **统计信息**: http://localhost:5000/api/stats

## 🎯 首次使用步骤

1. **启动后端** → 会自动获取一次新闻
2. **打开前端** → 应该看到新闻列表
3. **点击"刷新"按钮** → 手动更新新闻

## ⚙️ 定时任务配置

后端会自动在以下时间获取新闻：
- **08:00** 早晨
- **12:00** 中午
- **18:00** 下午
- **22:00** 晚上
- **每30分钟** 定时检查一次

所有任务执行日志保存在 `backend/data/scheduler.log`

## 📝 新增新闻源

编辑 `backend/scrapers/news_scraper.py`：

### 添加RSS源（推荐）

```python
# 在 NewsAggregator.scrapers 中添加
from scrapers.news_scraper import RSSNewsScraper

scraper = RSSNewsScraper('https://example.com/feed.xml', 'My News')
news = scraper.parse_news()
```

### 常用RSS源
- BBC: http://feeds.bbc.co.uk/news/rss.xml
- Reuters: https://www.reuters.com/finance
- CNN: http://rss.cnn.com/rss/edition.rss
- HackerNews: https://news.ycombinator.com/rss

## 🐛 常见问题

### Q: 前端显示"无法连接后端"
**A:** 
1. 确认Flask服务在 http://localhost:5000 运行
2. 查看浏览器控制台错误信息
3. 检查防火墙设置

### Q: 新闻列表为空
**A:**
1. 点击"刷新"按钮手动获取新闻
2. 检查网络连接
3. 查看后端控制台是否有错误信息

### Q: 定时任务不执行
**A:**
1. 检查 `scheduler.py` 是否在运行
2. 查看 `backend/data/scheduler.log` 日志
3. 确认系统时间设置正确

### Q: 爬虫超时
**A:**
1. 检查网络连接速度
2. 增加超时时间：编辑 `backend/config.py` 中的 `SCRAPER_TIMEOUT`
3. 检查RSS源是否仍有效

## 🚀 下一步

- 添加更多新闻源
- 自定义样式和主题
- 部署到服务器
- 添加数据库存储
- 实现用户账户系统
- 添加搜索和推荐功能

## 📞 获取帮助

- 查看完整文档：[README.md](README.md)
- 查看API文档：[README.md#-api文档](README.md#-api文档)
- 查看代码注释

---

**祝你使用愉快！** 🎉
