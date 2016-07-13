# Chap08/httpbin_client.py
import json
import requests

class HeadersModel(object):

    def __init__(self, data):
        self.host = data['headers']['Host']
        self.user_agent = data['headers']['User-Agent']
        self.accept = data['headers']['Accept']

class HttpBinClient(object):

    base_url = 'http://httpbin.org'

    def get_ip(self):
        response = requests.get("{}/ip".format(self.base_url))
        my_ip = response.json()['origin']
        return my_ip

    def get_user_agent(self):
        response = requests.get("{}/user-agent".format(self.base_url))
        user_agent = response.json()['user-agent']
        return user_agent

    def get_headers(self):
        response = requests.get("{}/headers".format(self.base_url))
        headers = HeadersModel(response.json())
        return headers

    def get_image(self, image_format):
        image_map = {
            'png': 'image/png',
            'jpg': 'image/jpg'
        }
        try:
            headers = {'Accept': image_map[image_format]}
        except KeyError:
            raise Exception("Format {} not valid".format(image_format))
        r = requests.get("{}/image", headers=headers)

if __name__ == '__main__':
    http_bin = HttpBinClient()

    my_ip = http_bin.get_ip()
    user_agent = http_bin.get_user_agent()
