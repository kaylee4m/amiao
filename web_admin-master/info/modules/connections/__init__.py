
# 创建蓝图对象
from flask import Blueprint

connection_blu = Blueprint('connection', __name__)

from . import views