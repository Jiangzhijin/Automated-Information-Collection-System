#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""查找正确的VOA中文RSS源"""

import feedparser

# 尝试多个可能的VOA中文RSS源
voa_urls = [
    'https://www.voachinese.com/api/z-6tqlbtz6jga',
    'https://www.voachinese.com/api/z-$y_ye_v-iv',
    'https://www.voachinese.com/api/rss/news-zh-hans',
    'https://feeds.voachinese.com/feed',
    'https://www.voa.gov/feeds/chinese',
]

print("尝试查找VOA中文RSS源...\n")

for url in voa_urls:
    try:
        feed = feedparser.parse(url)
        entries = len(feed.entries)
        print(f"✓ {url}")
        print(f"  条目数: {entries}")
        if entries > 0:
            print(f"  ✅ 成功! 第一条: {feed.entries[0].get('title', '')[:50]}")
            print()
        else:
            print()
    except Exception as e:
        print(f"✗ {url}")
        print(f"  错误: {str(e)}\n")

# 尝试爬取主页面
print("\n尝试爬取VOA中文主页...")
try:
    import requests
    from bs4 import BeautifulSoup
    
    resp = requests.get('https://www.voachinese.com', timeout=10)
    print(f"HTTP状态: {resp.status_code}")
    
    # 查找RSS链接
    soup = BeautifulSoup(resp.text, 'html.parser')
    links = soup.find_all('link', {'type': 'application/rss+xml'})
    print(f"找到 {len(links)} 个RSS链接:")
    for link in links[:3]:
        print(f"  - {link.get('href', '')}")
except Exception as e:
    print(f"错误: {e}")
