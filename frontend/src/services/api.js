import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
});

// 新闻服务
export const newsService = {
  // 获取新闻列表
  getNews: (page = 1, perPage = 20, source = '') => {
    return api.get('/news', {
      params: { page, per_page: perPage, source }
    });
  },

  // 刷新新闻
  refreshNews: () => {
    return api.post('/news/refresh');
  },

  // 获取统计信息
  getStats: () => {
    return api.get('/stats');
  },

  // 健康检查
  healthCheck: () => {
    return api.get('/health');
  }
};

export default api;
