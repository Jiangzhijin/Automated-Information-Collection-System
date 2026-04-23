# 🎯 信息汇总网站 - 用户快速开始指南

## 📌 一分钟快速启动

### 选项 1: Windows PowerShell（推荐）
```powershell
cd c:\Users\wei23\OneDrive\桌面\信息处理
$env:DANGEROUSLY_DISABLE_HOST_CHECK="true"

# 终端 1：启动后端
python backend/app/app.py

# 终端 2：启动前端
cd frontend
npm start
```

### 选项 2: 双击启动 (Windows)
创建快捷方式并运行:
```cmd
@echo off
cd /d c:\Users\wei23\OneDrive\桌面\信息处理
start cmd /k "python backend/app/app.py"
timeout /t 2
start cmd /k "cd frontend && set DANGEROUSLY_DISABLE_HOST_CHECK=true && npm start"
```

### 选项 3: Docker
```bash
cd c:\Users\wei23\OneDrive\桌面\信息处理
docker-compose up
```

## 🌐 访问网站

启动后，在浏览器中打开:
```
http://localhost:3000
```

## 📰 新闻源说明

| 源名 | 简介 | 更新频率 |
|------|------|---------|
| **BBC 中文** 🇬🇧 | 英国广播公司中文版，权威的国际新闻 | 实时 |
| **德国之声** 🇩🇪 | 德国国际广播电台，提供多语言国际新闻 | 实时 |
| **RFI** 🇫🇷 | 法国国际广播电台，专业的国际新闻报道 | 实时 |
| **卫报** 🇬🇧 | 英国老牌媒体，全球新闻覆盖 | 实时 |

## 🎮 使用功能

### 1. 浏览新闻
- 新闻以网格卡片显示
- 点击卡片右下方的 "阅读链接" 按钮可以打开原文

### 2. 分页浏览
- 使用底部分页控制查看更多新闻
- **首页** - 第一页
- **上一页** - 上一页
- **页码** - 显示当前页
- **下一页** - 下一页  
- **末页** - 最后一页

### 3. 按源过滤
- 页面右上方有 "新闻源" 下拉菜单
- 选择特定源只显示该源的新闻
- 选择 "全部" 显示所有新闻

### 4. 手动刷新
- 点击右上方的 🔄 刷新按钮
- 系统将立即从所有源获取最新新闻

### 5. 查看统计
- 页面上方显示:
  - 📊 总新闻数
  - 📡 新闻源个数
  - ⏰ 最后更新时间

## 📊 统计信息

- **总新闻数**: 通常 80-100+ 条
- **更新频率**: 自动每 30 分钟更新 + 每日 4 次固定时间
- **源数量**: 4 个国际知名媒体
- **覆盖地区**: 全球国际新闻

## 🔧 常见问题

### Q1: 页面刷新后没有新闻怎么办？
**A**: 等待 5-10 秒，让后端获取新闻。或点击页面右上方的刷新按钮。

### Q2: 某个新闻源没有显示新闻？
**A**: 可能是该源暂时不可用。系统会在下次自动更新时重试。

### Q3: 如何更改刷新频率？
**A**: 编辑 `backend/app/scheduler.py` 文件中的计划任务配置。

### Q4: 新闻太多/太少了？
**A**: 可以修改 `backend/scrapers/news_scraper.py` 中每个源的获取条数。

### Q5: 如何添加新的新闻源？
**A**: 在 `backend/scrapers/news_scraper.py` 中创建新的 Scraper 类，然后在 NewsAggregator 的 __init__ 方法中添加。

## 📁 重要文件位置

```
c:\Users\wei23\OneDrive\桌面\信息处理\
├── 新闻数据
│   └── backend/data/all_news.json          ← 所有新闻数据
│
├── 源代码
│   ├── backend/app/app.py                  ← Flask API
│   ├── backend/scrapers/news_scraper.py    ← 爬虫逻辑
│   └── frontend/src/components/NewsList.jsx ← React 组件
│
├── 配置文件
│   ├── backend/requirements.txt             ← Python 依赖
│   └── frontend/package.json                ← Node 依赖
│
└── 文档
    ├── README.md                            ← 项目文档
    ├── FINAL_REPORT.md                      ← 最终报告
    └── SYSTEM_STATUS.md                     ← 系统状态
```

## 🌟 高级用途

### 手动获取新闻
```bash
cd backend
python fetch_news.py
```

### 测试单个源
```bash
cd backend
python find_all_sources.py
```

### 查看 API 响应
```bash
curl http://localhost:5000/api/stats
curl "http://localhost:5000/api/news?page=1&per_page=20"
```

### 后台运行 (Linux/Mac)
```bash
nohup python backend/app/app.py &
nohup npm start --prefix frontend &
```

## 🎨 自定义UI

### 修改颜色主题
编辑 `frontend/src/components/NewsList.jsx`
```javascript
// 找到 gradient 样式
background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
// 修改为你喜欢的颜色
```

### 修改新闻数量
编辑 `backend/scrapers/news_scraper.py`
```python
for entry in feed.entries[:20]:  # 改这个数字
```

### 修改分页大小
编辑 `frontend/src/components/NewsList.jsx`
```javascript
const per_page = 20;  // 改这个数字
```

## 📞 技术支持

如遇到问题:
1. 检查 `backend/data/scheduler.log` 了解自动更新日志
2. 确认后端和前端都已启动
3. 查看浏览器控制台 (F12) 的错误信息
4. 检查网络连接是否正常

## 💡 提示

- 💾 新闻数据自动保存，即使服务重启也不会丢失
- 🔒 数据以 JSON 格式存储，可以轻松导出分享
- 🚀 性能优秀，支持数百条新闻流畅加载
- 📱 完全响应式，任何设备上都能完美显示

---

**祝您使用愉快！** 🎉

有任何问题，请参考项目文档:
- README.md - 完整项目文档
- SYSTEM_STATUS.md - 系统状态详解
- FINAL_REPORT.md - 最终项目报告
