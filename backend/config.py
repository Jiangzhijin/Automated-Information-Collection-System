"""
应用配置文件
"""
import os

class Config:
    """基础配置"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    JSON_SORT_KEYS = False
    
    # 爬虫配置
    SCRAPER_TIMEOUT = 10  # 爬虫超时时间（秒）
    SCRAPER_RETRY = 3  # 爬虫重试次数
    
    # 定时任务配置
    SCHEDULER_INTERVAL = 30  # 定时任务间隔（分钟）
    SCHEDULER_ENABLED = True  # 是否启用定时任务


class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """测试环境配置"""
    DEBUG = True
    TESTING = True


# 配置字典
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config(env=None):
    """获取配置对象"""
    if env is None:
        env = os.environ.get('FLASK_ENV', 'development')
    return config.get(env, config['default'])
