import cv2
import requests
import pickle as pkl

class RequestClient(object):
    def __init__(self, url):
        self.url = url
    def send(self, data):
        content = None
        if type(data) != bytes:
            data = pkl.dumps(data)
        res = requests.post(self.url, data)
        if res.status_code != 200:
            return None
        if res.content is None:
            return None
        else:
            try:
                content = pkl.loads(res.content)
            except Exception as e:
                return None
        return content
