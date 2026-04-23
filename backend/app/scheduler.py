"""
定时任务调度器 - 自动定时获取新闻
"""
import sys
import os
import logging
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scrapers.news_scraper import NewsAggregator

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(os.path.dirname(__file__), '..', 'data', 'scheduler.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class NewsScheduler:
    """新闻定时获取调度器"""
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.aggregator = NewsAggregator()
        self.is_running = False
    
    def fetch_news_job(self):
        """定时任务 - 获取新闻"""
        try:
            logger.info("开始获取新闻...")
            news_data = self.aggregator.save_news()
            logger.info(f"成功获取 {news_data['total']} 条新闻")
            logger.info(f"新闻源: {', '.join(news_data['sources'])}")
        except Exception as e:
            logger.error(f"获取新闻出错: {str(e)}")
    
    def start(self, interval_minutes: int = 30):
        """启动调度器"""
        if self.is_running:
            logger.warning("调度器已在运行中")
            return
        
        # 添加定时任务 - 每隔指定分钟执行一次
        self.scheduler.add_job(
            self.fetch_news_job,
            'interval',
            minutes=interval_minutes,
            id='fetch_news_job',
            name='定时获取新闻'
        )
        
        # 添加每天特定时间的任务
        # 早上8点、中午12点、晚上6点、晚上10点各更新一次
        times = ['08:00', '12:00', '18:00', '22:00']
        for i, time_str in enumerate(times):
            hour, minute = map(int, time_str.split(':'))
            self.scheduler.add_job(
                self.fetch_news_job,
                CronTrigger(hour=hour, minute=minute),
                id=f'scheduled_news_{i}',
                name=f'每日 {time_str} 更新新闻'
            )
        
        self.scheduler.start()
        self.is_running = True
        logger.info(f"新闻定时任务已启动，间隔: {interval_minutes}分钟")
        logger.info("定时任务: 每日 08:00, 12:00, 18:00, 22:00 自动更新新闻")
    
    def stop(self):
        """停止调度器"""
        if not self.is_running:
            logger.warning("调度器未在运行")
            return
        
        self.scheduler.shutdown()
        self.is_running = False
        logger.info("定时任务已停止")
    
    def get_jobs(self):
        """获取所有任务信息"""
        jobs = []
        for job in self.scheduler.get_jobs():
            jobs.append({
                'id': job.id,
                'name': job.name,
                'next_run_time': str(job.next_run_time)
            })
        return jobs


# 全局调度器实例
news_scheduler = NewsScheduler()


if __name__ == '__main__':
    print("启动新闻定时获取服务...")
    
    # 立即执行一次
    news_scheduler.fetch_news_job()
    
    # 启动定时任务（每30分钟一次，加上特定时间更新）
    news_scheduler.start(interval_minutes=30)
    
    print("定时任务运行中，按 Ctrl+C 停止...")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\\n停止服务...")
        news_scheduler.stop()
