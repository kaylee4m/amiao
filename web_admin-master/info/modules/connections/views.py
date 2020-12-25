from flask import request, jsonify, current_app
from info.modules.connections import connection_blu
import datetime

from info.utills.MockTool import MockData

from info.utills.RequestClientTool import RequestClient
from info.utills.response_code import RET

@connection_blu.route('/connection_test', methods=['GET'])
def connection_test():
    server_ip = '192.168.8.124:80'
    
    # dis_url = 'http://{}/person/get_persons'.format(server_ip)
    dis_url = 'http://{}/person/get_head_leg_body'.format(server_ip)
    client = RequestClient(dis_url)
    mock = MockData()
    img_byte = mock.imgbytes('person2')
    # bbox_listmock.bbox_list()
    ticks = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {}
    data['dis_url'] = dis_url
    data['date'] = ticks
    try:
        # results = client.send([img_byte,bbox_list])
        results = client.send(img_byte)
        print(results)
        if results:
            data['states'] = 'True'
            return jsonify(errno=RET.OK, errmsg="OK", data=data)
        else:
            data['states'] = 'False'
            return jsonify(errno=RET.NODATA, errmsg="nodata", data=data)
    except Exception as e:
        current_app.logger.error(e)
        data['states'] = 'False'
        return jsonify(errno=RET.UNKOWNERR, errmsg="端口错误", data=data)
    
