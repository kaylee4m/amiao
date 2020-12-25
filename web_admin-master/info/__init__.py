import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request
from flask_babel import Babel
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask_cors import *

from configs import config

# 初始化数据库
db = SQLAlchemy()
redis_store = None   # type:# StrictRedis
# redis_store:StrictRedis = None
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin') or 'http://127.0.0.1:9528'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization,Accept,Origin,Referer,User-Agent'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

def setup_log(config_name):
    # 设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)

def create_app(config_name):
    # 配置日志
    setup_log(config_name)

    # 创建flask对象
    app = Flask(__name__)
    # CORS(app, supports_credentials=True)
    # 国际化配置
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

    babel = Babel(app)

    @babel.localeselector
    def get_locale():  # 核心，当网站含有locale的cookie，且符合['zh', 'en']
        cookie = request.cookies.get('locale')
        if cookie in ['zh', 'en']:
            return cookie
        return request.accept_languages.best_match(app.config.get('BABEL_DEFAULT_LOCALE'))

    # 加载配置
    app.config.from_object(config[config_name])

    app.config['JSON_AS_ASCII'] = False

    # 通过app初始化
    db.init_app(app)

    # 初始化redis存储对象
    global redis_store
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)

    # 开启CSRF保护,只做服务器验证功能
    # CSRFProtect(app)

    # 设置Session保存位置
    Session(app)
    CORS(app)
    # 注册蓝图

    from info.modules.camera import camera_blu
    app.register_blueprint(camera_blu)

    
    from info.modules.connections import connection_blu
    app.register_blueprint(connection_blu)

    return app