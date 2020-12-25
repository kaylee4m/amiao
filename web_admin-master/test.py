from info.utills.MockTool import MockData

from info.utills.RequestClientTool import RequestClient

server_ip = '182.168.8.124:80'
dis_url = 'http://{}/person/get_persons'.format(server_ip)
client = RequestClient(dis_url)

mock = MockData()
img_byte = mock.imgbytes('person1')
client.send(img_byte)

