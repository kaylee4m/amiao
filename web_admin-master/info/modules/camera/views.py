import os
import re
import telnetlib

from flask import request, jsonify, current_app
from info.modules.camera import camera_blu
from info.utills.response_code import RET
from info.utills.camera import VideoCamera


@camera_blu.route('/camera_before', methods=['GET'])
def camera_before():
    # url_n = request.args.get('url_name')
    url_n = 'rtsp://admin:hr123456@192.168.8.106:554/h264/ch1/sub/av_stream'
    if not url_n:
        return jsonify(errno=RET.NODATA, errmsg="无数据")
    url_name = str(url_n)
#     reobj = re.compile(r'''(?x)\A[a-z][a-z0-9+\-.]*://( [a-z][a-z0-9+\-.]*):([a-z0-9\-._~%!$&'()*+,;=]+)@?([a-z0-9\-._~%]+|\[[a-z0-9\-._~%!$&'()*+,;=:]+\])
# :(?P<port>[0-9]+)''')
    reobj = re.compile(r'''(?x)\A[a-z][a-z0-9+\-.]*://( .+):([a-z0-9\-._~%!$&'()*+,;=]+)@?([a-z0-9\-._~%]+|\[[a-z0-9\-._~%!$&'()*+,;=:]+\])
:(?P<port>[0-9]+)''')
    user_name = reobj.search(url_name).group(1)
    password = reobj.search(url_name).group(2)
    ip = reobj.search(url_name).group(3)
    port = reobj.search(url_name).group(4)
    data = {}
    data['user_name'] = user_name
    data['password'] = password
    data['ip'] = ip
    data['port'] = port
    try:
        telnetlib.Telnet(ip, port=port)
        data['telnet_state'] = 'True'
    except Exception as e:
        current_app.logger.error(e)
        data['telnet_state'] = 'False'
        data['opencv_state'] = 'False'
        return jsonify(errno=RET.PORTERR, errmsg="端口错误", data=data)

    camera = VideoCamera(url_n)
    frame = camera.get_frame()
    if frame:
        data['opencv_state'] = 'True'
        return jsonify(errno=RET.OK, errmsg="OK", data=data)
    else:
        data['opencv_state'] = 'False'
        # return data
        return jsonify(errno=RET.IOERR, errmsg="Camera Error", data=data)