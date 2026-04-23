#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""查找更多国际新闻源"""

import feedparser

# 尝试更多国际新闻源
more_sources = {
    'BBC 中文': 'https://www.bbc.com/zhongwen/simp/index.xml',
    '德国之声': 'https://rss.dw.com/xml/rss-chi-all',
    'RFI': 'https://www.rfi.fr/cn/rss/',
    '英国卫报': 'https://www.theguardian.com/world/rss',
    'NPR': 'https://feeds.npr.org/1001/rss.xml',
    'CNN': 'http://feeds.cnn.com/rss/edition.rss',
    '多国语言新闻': 'https://feeds.bloomberg.com/markets/news.rss',
    'AP通讯社': 'https://apnews.com/hub/ap-top-news/feed',
}

print("查找发达国家新闻源...\n")

valid_sources = {}
for name, url in more_sources.items():
    try:
        feed = feedparser.parse(url)
        entries = len(feed.entries)
        if entries > 0:
            valid_sources[name] = (url, entries)
            print(f"✅ {name}: {entries} 条条目")
            print(f"   {url}\n")
    except Exception as e:
        print(f"❌ {name}: {e}\n")

print(f"\n总共找到 {len(valid_sources)} 个有效源")
print("\n推荐使用的源:")
for name, (url, count) in sorted(valid_sources.items(), key=lambda x: x[1][1], reverse=True)[:5]:
    print(f"  - {name} ({count} 条条目)")
