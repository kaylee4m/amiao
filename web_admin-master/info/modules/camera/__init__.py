
# 创建蓝图对象
from flask import Blueprint

camera_blu = Blueprint('camera', __name__)

from . import views