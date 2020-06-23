import unittest
import requests
import sys
import json
import ddt
from BeautifulReport import BeautifulReport


test_base = 'http://localhost:8888/'
http_head = 'http://'

global s
s = requests.session()

def request_return(
        url="http://localhost:8888/",
        method='POST',
        jsonInput=None,
        parameInput=None,
        cookieInput=None
        ):
        global s
        if method == 'POST':
            r = s.post(url, json=jsonInput, params=parameInput, cookies=cookieInput)
        elif method == 'GET':
            r = s.get(url, json=jsonInput, params=parameInput, cookies=cookieInput)
        else:
            pass
        return r

def log_print(url, method, response):
    print(str(response.status_code) + '    To ' + url + '  ' + '  ' + method)
    print(json.dumps(dict(response.headers)))
    print(response.text)
    print('\n')


