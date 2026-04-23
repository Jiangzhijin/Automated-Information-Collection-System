"""
Flask API 服务器 - 提供新闻数据接口
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json
import os
import sys

# 添加scrapers模块路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scrapers.news_scraper import NewsAggregator

app = Flask(__name__)
CORS(app)  # 启用跨域请求

# 全局爬虫实例
aggregator = NewsAggregator()


@app.route('/api/news', methods=['GET'])
def get_news():
    """获取所有新闻"""
    try:
        # 获取分页参数
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        source = request.args.get('source', '', type=str)
        
        # 读取本地新闻数据
        data_file = os.path.join(os.path.dirname(__file__), 'data', 'all_news.json')
        
        if os.path.exists(data_file):
            with open(data_file, 'r', encoding='utf-8') as f:
                news_data = json.load(f)
        else:
            # 如果没有本地文件，实时获取
            news_data = aggregator.fetch_all_news()
        
        articles = news_data.get('articles', [])
        
        # 按源筛选
        if source:
            articles = [a for a in articles if source.lower() in a.get('source', '').lower()]
        
        # 分页
        total = len(articles)
        start = (page - 1) * per_page
        end = start + per_page
        
        paginated_articles = articles[start:end]
        
        return jsonify({
            'status': 'success',
            'data': paginated_articles,
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': total,
                'pages': (total + per_page - 1) // per_page
            },
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/news/refresh', methods=['POST'])
def refresh_news():
    """手动刷新新闻"""
    try:
        news_data = aggregator.save_news()
        return jsonify({
            'status': 'success',
            'message': f'成功获取 {news_data["total"]} 条新闻',
            'total': news_data['total'],
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """获取统计信息"""
    try:
        data_file = os.path.join(os.path.dirname(__file__), 'data', 'all_news.json')
        
        if os.path.exists(data_file):
            with open(data_file, 'r', encoding='utf-8') as f:
                news_data = json.load(f)
        else:
            news_data = aggregator.fetch_all_news()
        
        # 统计各源的新闻数量
        sources_count = {}
        for article in news_data.get('articles', []):
            source = article.get('source', 'Unknown')
            sources_count[source] = sources_count.get(source, 0) + 1
        
        return jsonify({
            'status': 'success',
            'total_articles': news_data.get('total', 0),
            'sources': news_data.get('sources', []),
            'sources_count': sources_count,
            'last_update': news_data.get('timestamp', '')
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """健康检查"""
    return jsonify({
        'status': 'ok',
        'timestamp': datetime.now().isoformat()
    })


@app.errorhandler(404)
def not_found(error):
    """404 错误处理"""
    return jsonify({
        'status': 'error',
        'message': '资源不存在'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """500 错误处理"""
    return jsonify({
        'status': 'error',
        'message': '内部服务器错误'
    }), 500


if __name__ == '__main__':
    # 初始化数据
    print("初始化新闻数据...")
    aggregator.save_news()
    
    # 启动Flask应用
    app.run(debug=True, host='0.0.0.0', port=5000)
