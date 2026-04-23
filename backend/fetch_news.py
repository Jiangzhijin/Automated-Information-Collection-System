#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""测试新闻源"""

from scrapers.news_scraper import NewsAggregator

print("开始获取新闻...")
aggregator = NewsAggregator()
news_data = aggregator.save_news()

print(f"\n✅ 成功获取 {news_data['total']} 条新闻")
print(f"📰 新闻源: {', '.join(news_data['sources'])}")
print("\n前5条新闻:")
for i, article in enumerate(news_data['articles'][:5], 1):
    print(f"\n{i}. [{article['source']}] {article['title'][:60]}...")
