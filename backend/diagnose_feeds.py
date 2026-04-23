#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""诊断新闻源"""

import feedparser
import requests

sources = {
    'BBC 中文': 'https://www.bbc.com/zhongwen/simp/index.xml',
    'DW 中文': 'https://rss.dw.com/xml/rss-chi-all',
    '美国之音 (top)': 'https://www.voachinese.com/z/1593',
    '美国之音 (usa)': 'https://www.voachinese.com/z/2025',
    '美国之音 (world)': 'https://www.voachinese.com/z/2026'
}

for name, url in sources.items():
    print(f"\n{'='*60}")
    print(f"测试: {name}")
    print(f"URL:  {url}")
    print('-'*60)
    
    try:
        # 测试HTTP连接
        r = requests.get(url, timeout=10)
        print(f"✅ HTTP状态: {r.status_code}")
        
        # 测试feedparser解析
        feed = feedparser.parse(url)
        entries = len(feed.entries)
        print(f"✅ 条目数: {entries}")
        
        if entries > 0:
            print(f"第一条: {feed.entries[0].get('title', '无标题')[:60]}")
        else:
            print("⚠️  无条目")
            
    except Exception as e:
        print(f"❌ 错误: {str(e)}")
