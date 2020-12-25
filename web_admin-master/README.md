# 需求

1. 算法接口心跳/手动检测
2. 摄像头管理

# 数据模型
===========================
## Camera
id : int, primary key
url: str, ''
location: str, ''
telnet_status: bool, False
opencv_status: bool, False

## Service
id: int, primary key
url: str, ''
description, str, ''


## CamServ
'''构建Camera和Service多对多关系'''
id: int, primary key
Camera: foreign key, Camera
Service: foreign key, Service


## 接口

add_camera()

modify_camera()

get_camera()

del_camera()

check_camera()

add_service()

modify_service()

get_service()

del_service()

add_camsev()

modify_camsev()

get_camsev()

del_camsev()
