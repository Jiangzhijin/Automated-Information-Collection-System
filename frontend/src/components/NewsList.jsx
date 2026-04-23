import React, { useState, useEffect } from 'react';
import { FiRefreshCw, FiExternalLink, FiCalendar } from 'react-icons/fi';
import { newsService } from '../services/api';
import './NewsList.css';

export default function NewsList() {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(false);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [stats, setStats] = useState(null);
  const [selectedSource, setSelectedSource] = useState('');
  const [error, setError] = useState(null);

  // 获取新闻列表
  const fetchNews = async (pageNum = 1) => {
    try {
      setLoading(true);
      setError(null);
      const response = await newsService.getNews(pageNum, 20, selectedSource);
      const { data, pagination } = response.data;
      setNews(data);
      setPage(pagination.page);
      setTotalPages(pagination.pages);
    } catch (err) {
      setError('获取新闻失败，请检查后端服务是否运行');
      console.error('获取新闻错误:', err);
    } finally {
      setLoading(false);
    }
  };

  // 获取统计信息
  const fetchStats = async () => {
    try {
      const response = await newsService.getStats();
      setStats(response.data);
    } catch (err) {
      console.error('获取统计信息错误:', err);
    }
  };

  // 刷新新闻
  const handleRefresh = async () => {
    try {
      setLoading(true);
      await newsService.refreshNews();
      fetchNews(1);
      fetchStats();
    } catch (err) {
      setError('刷新新闻失败');
      console.error('刷新错误:', err);
    } finally {
      setLoading(false);
    }
  };

  // 初始加载
  useEffect(() => {
    fetchNews(1);
    fetchStats();
  }, []);

  // 源过滤变化
  useEffect(() => {
    setPage(1);
    fetchNews(1);
  }, [selectedSource]);

  // 格式化日期
  const formatDate = (dateString) => {
    if (!dateString) return '时间未知';
    const date = new Date(dateString);
    if (isNaN(date)) return dateString;
    return date.toLocaleDateString('zh-CN', {
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <div className="news-list-container">
      {/* 头部 */}
      <header className="header">
        <div className="header-content">
          <h1>📰 信息汇总</h1>
          <p className="subtitle">实时新闻聚合平台</p>
        </div>
        <button
          className="refresh-btn"
          onClick={handleRefresh}
          disabled={loading}
          title="刷新新闻"
        >
          <FiRefreshCw size={20} className={loading ? 'spinning' : ''} />
          <span>{loading ? '更新中...' : '刷新'}</span>
        </button>
      </header>

      {/* 错误提示 */}
      {error && (
        <div className="error-message">
          ⚠️ {error}
        </div>
      )}

      {/* 统计信息 */}
      {stats && (
        <div className="stats-card">
          <div className="stat-item">
            <span className="stat-label">总新闻数</span>
            <span className="stat-value">{stats.total_articles}</span>
          </div>
          <div className="stat-item">
            <span className="stat-label">新闻源</span>
            <span className="stat-value">{stats.sources.length}</span>
          </div>
          <div className="stat-item">
            <span className="stat-label">最后更新</span>
            <span className="stat-value">{formatDate(stats.last_update)}</span>
          </div>
        </div>
      )}

      {/* 源选择过滤 */}
      {stats && stats.sources.length > 0 && (
        <div className="filter-section">
          <label htmlFor="source-filter">按来源筛选:</label>
          <select
            id="source-filter"
            value={selectedSource}
            onChange={(e) => setSelectedSource(e.target.value)}
            className="source-filter"
          >
            <option value="">全部来源</option>
            {stats.sources.map((source) => (
              <option key={source} value={source}>
                {source} ({stats.sources_count[source]})
              </option>
            ))}
          </select>
        </div>
      )}

      {/* 新闻列表 */}
      <div className="news-grid">
        {loading && <div className="loading">加载中...</div>}
        {!loading && news.length === 0 && (
          <div className="no-news">暂无新闻数据，请刷新或检查后端服务</div>
        )}
        {!loading && news.map((article, index) => (
          <article key={index} className="news-card">
            <div className="news-header">
              <h3 className="news-title">{article.title}</h3>
              <span className="news-source">{article.source}</span>
            </div>
            <p className="news-description">{article.description}</p>
            <div className="news-footer">
              <span className="news-date">
                <FiCalendar size={14} />
                {formatDate(article.published || article.timestamp)}
              </span>
              {article.link && (
                <a
                  href={article.link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="news-link"
                >
                  阅读全文 <FiExternalLink size={14} />
                </a>
              )}
            </div>
          </article>
        ))}
      </div>

      {/* 分页 */}
      {totalPages > 1 && (
        <div className="pagination">
          <button
            onClick={() => fetchNews(1)}
            disabled={page === 1 || loading}
          >
            首页
          </button>
          <button
            onClick={() => fetchNews(page - 1)}
            disabled={page === 1 || loading}
          >
            上一页
          </button>
          <span className="page-info">
            第 {page} / {totalPages} 页
          </span>
          <button
            onClick={() => fetchNews(page + 1)}
            disabled={page === totalPages || loading}
          >
            下一页
          </button>
          <button
            onClick={() => fetchNews(totalPages)}
            disabled={page === totalPages || loading}
          >
            末页
          </button>
        </div>
      )}
    </div>
  );
}
