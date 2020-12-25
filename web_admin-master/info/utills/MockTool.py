import os
import random

def read_img_file_to_bytes(img_path):
    img_file = open(img_path, 'rb')
    img_byte = img_file.read()
    img_file.close()
    return img_byte

server_ip = 'http://my_nginx:80'            

class MockData(object):
    def __init__(self):
        self.imgs = {
            'person1': 'info/utills/images/42200_960.jpg',
            'person2': 'info/utills/images/persons.jpg',
            'meter': 'info/utills/images/1.jpg',
            'fire': 'info/utills/images/fire.jpg',
            'helmet': 'info/utills/images/helmet.jpg'
        }

    def imgbytes(self, img_type):
        assert isinstance(img_type, str)
        assert img_type in self.imgs, '必须在图片列表中'
        img_path = self.imgs.get(img_type)
        if img_path is None:
            raise ValueError("{} 图片没有注册".format(img_type))
        return read_img_file_to_bytes(img_path)

    def imgbytes_list(self, img_type, length):
        assert isinstance(length, int)
        img = self.imgbytes(img_type)
        ret = []
        for i in range(length):
            ret.append(img)
        return ret

    def bbox_list(self, length, xmax=100, ymax=100, int_out=False):
        assert isinstance(length, int)
        ret = []
        for i in range(length):
            ret.append([5,25,5,25])
        return ret

