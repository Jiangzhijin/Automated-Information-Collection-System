"""
新闻爬虫模块 - 支持API和网页爬虫
"""
import requests
import feedparser
from datetime import datetime
from typing import List, Dict
import json
import os
from bs4 import BeautifulSoup

class NewsScraperBase:
    """爬虫基类"""
    def __init__(self):
        self.news_list = []
    
    def parse_news(self) -> List[Dict]:
        """解析新闻，子类实现"""
        raise NotImplementedError
    
    def save_to_file(self, data: List[Dict], filename: str):
        """保存到JSON文件"""
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        os.makedirs(data_dir, exist_ok=True)
        
        filepath = os.path.join(data_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


class RSSNewsScraper(NewsScraperBase):
    """RSS源新闻爬虫"""
    def __init__(self, rss_url: str, source_name: str):
        super().__init__()
        self.rss_url = rss_url
        self.source_name = source_name
    
    def parse_news(self) -> List[Dict]:
        """解析RSS源"""
        try:
            feed = feedparser.parse(self.rss_url)
            news_list = []
            
            for entry in feed.entries[:20]:  # 获取最新20条
                news_item = {
                    'title': entry.get('title', ''),
                    'link': entry.get('link', ''),
                    'description': entry.get('summary', '')[:200],  # 摘要
                    'source': self.source_name,
                    'published': entry.get('published', ''),
                    'timestamp': datetime.now().isoformat()
                }
                news_list.append(news_item)
            
            return news_list
        except Exception as e:
            print(f"爬虫错误 ({self.source_name}): {str(e)}")
            return []


class BBCChineseScraper(NewsScraperBase):
    """BBC 中文网爬虫"""
    def __init__(self):
        super().__init__()
        self.rss_url = 'https://www.bbc.com/zhongwen/simp/index.xml'
    
    def parse_news(self) -> List[Dict]:
        scraper = RSSNewsScraper(self.rss_url, 'BBC 中文')
        return scraper.parse_news()


class RFIScraper(NewsScraperBase):
    """RFI 法国国际广播电台中文爬虫"""
    def __init__(self):
        super().__init__()
        self.rss_url = 'https://www.rfi.fr/cn/rss/'
    
    def parse_news(self) -> List[Dict]:
        scraper = RSSNewsScraper(self.rss_url, 'RFI')
        return scraper.parse_news()


class DWChineseScraper(NewsScraperBase):
    """德国之声中文网爬虫"""
    def __init__(self):
        super().__init__()
        self.rss_url = 'https://rss.dw.com/xml/rss-chi-all'
    
    def parse_news(self) -> List[Dict]:
        scraper = RSSNewsScraper(self.rss_url, '德国之声')
        return scraper.parse_news()


class GuardianScraper(NewsScraperBase):
    """英国卫报国际新闻爬虫"""
    def __init__(self):
        super().__init__()
        self.rss_url = 'https://www.theguardian.com/world/rss'
    
    def parse_news(self) -> List[Dict]:
        scraper = RSSNewsScraper(self.rss_url, '卫报')
        return scraper.parse_news()



class NewsAggregator:
    """新闻聚合器 - 整合多个新闻源"""
    def __init__(self):
        self.scrapers = [
            BBCChineseScraper(),
            DWChineseScraper(),
            RFIScraper(),
            GuardianScraper(),
        ]
    
    def fetch_all_news(self) -> Dict:
        """获取所有新闻源的新闻"""
        all_news = {
            'articles': [],
            'total': 0,
            'timestamp': datetime.now().isoformat(),
            'sources': []
        }
        
        for scraper in self.scrapers:
            try:
                news = scraper.parse_news()
                all_news['articles'].extend(news)
                # 获取源名称
                if news:
                    source_name = news[0]['source']
                    if source_name not in all_news['sources']:
                        all_news['sources'].append(source_name)
            except Exception as e:
                print(f"获取新闻失败: {str(e)}")
        
        # 按时间排序
        all_news['articles'].sort(
            key=lambda x: x.get('timestamp', ''),
            reverse=True
        )
        all_news['total'] = len(all_news['articles'])
        
        return all_news
    
    def save_news(self):
        """保存新闻到文件"""
        news_data = self.fetch_all_news()
        
        # 保存聚合的所有新闻
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        os.makedirs(data_dir, exist_ok=True)
        
        filepath = os.path.join(data_dir, 'all_news.json')
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(news_data, f, ensure_ascii=False, indent=2)
        
        return news_data


if __name__ == '__main__':
    # 测试爬虫
    aggregator = NewsAggregator()
    news = aggregator.save_news()
    print(f"成功获取 {news['total']} 条新闻")
    print(f"新闻源: {', '.join(news['sources'])}")
