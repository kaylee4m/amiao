import logging

import redis

class Configs(object):
    """工程配置信息"""
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"

    # DEBUG = True

    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@db:3306/rys"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 请求结束  自动执行db.session.commit
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # redis配置
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379

    # session 配置
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
    SESSION_PERMANENT = False  # 设置需要过期
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒
    # 设置日志等级
    LOG_LEVEL = logging.DEBUG


class DevelopementConfig(Configs):
    """开发环境下配置"""
    DEBUG = True


class ProductionConfig(Configs):
    """生产环境下配置"""
    DEBUG = False
    LOG_LEVEL = logging.WARNING


class TestingConfig(Configs):
    """单元测试环境下"""
    DEBUG = True
    TESTING = True


config = {
    'developement': DevelopementConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

# 实例化视频播放功能
# from info.utills.camera import Gen
# gen = Gen()
