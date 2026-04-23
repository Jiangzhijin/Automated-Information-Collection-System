#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""查找替代国际新闻源"""

import feedparser

# 尝试多个国际新闻源的RSS
alternative_sources = {
    'Reuters (路透社)': 'https://feeds.reuters.com/reuters/CNnews',
    '新华社': 'http://www.xinhuanet.com/rss/xinhuanet.xml',
    '环球时报': 'http://world.huanqiu.com/rss.shtml',
    'France24 中文': 'https://www.france24.com/zh/%E4%B8%AD%E6%96%87/rss',
    'RFI 法国国际广播电台': 'https://www.rfi.fr/cn/rss/',
    '日经新闻中文': 'https://cn.nikkei.com/news/rss.html',
}

print("尝试国际新闻源...\n")

for name, url in alternative_sources.items():
    try:
        feed = feedparser.parse(url)
        entries = len(feed.entries)
        status = "✅" if entries > 0 else "⚠️ "
        print(f"{status} {name}")
        print(f"   URL: {url}")
        print(f"   条目数: {entries}")
        if entries > 0:
            print(f"   第一条: {feed.entries[0].get('title', '')[:60]}")
        print()
    except Exception as e:
        print(f"❌ {name}")
        print(f"   错误: {e}\n")
