import ddt
import unittest
from baseOp import request_return, log_print, test_base

#-------------------------url block--------------------------#
login_urlp = 'login'
search_urlp = 'search'
search_hot_urlp = 'search/hot'
logout_urlp = 'logout'

#-------------------------test sets--------------------------#
test_data_login = [
    {'usr_no':'1859999', 'usr_password':'password'}
]
test_data_search = [
    {'text': '??', 'order': 'time', 'limit': 2},
    {'text': 'nb', 'order': 'rep'},
    {'text': 'lph', 'order': 'click', 'limit': 1}
]
test_data_search_hot = [
    {'bas_id': 1, 'tag_id': 2, 'limit': 100},
    {'bas_id': 2, 'limit': 4},
    {'tag_id': 3, 'limit': 6},
    {'bas_id': 3, 'tag_id': 1},
    {},
]
test_data_logout = [
    {'usr_no':'1859999', 'usr_password':'password'}
]

#-----------------------test segment--------------------------#
@ddt.ddt
class test07_search(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = test_base
        cls.logout_urlp = logout_urlp
        cls.login_urlp = login_urlp
        cls.search_urlp = search_urlp
        cls.search_hot_urlp = search_hot_urlp
        cls.r = None
        globals()['cksession'] = None

    # url: /login
    # generate cookies
    @ddt.data(*test_data_login)
    def test_0(self, data):
        self.r = request_return(
            url=self.base_url + self.login_urlp,
            method='POST',
            jsonInput=data
        )
        test07_search.cksession = dict(self.r.headers)['Set-Cookie'][8:40] # 8~40 is SJBBSID

    # url: /search
    # search sth. using LIKE
    #@unittest.skip
    @ddt.data(*test_data_search)
    def test_1(self, data):
        self.r = request_return(
            url=self.base_url + self.search_urlp,
            method='GET',
            jsonInput=data
        )
        log_print(
            url=self.base_url + self.search_urlp,
            method='GET',
            response=self.r
        )
        print('\n')

    # url: /search/hot
    # fetch hot posts only with 3 param: bas_id, tag_id, limit
    @ddt.data(*test_data_search_hot)
    def test_2(self, data):
        self.r = request_return(
            url=self.base_url + self.search_hot_urlp,
            method='GET',
            jsonInput=data
        )
        log_print(
            url=self.base_url + self.search_hot_urlp,
            method='GET',
            response=self.r
        )
        print('\n')

    # url: /logout
    # delete cookies while teardown
    @ddt.data(*test_data_logout)
    def test_99(self, data):
        self.r = request_return(
            url=test_base + logout_urlp,
            method='GET',
            jsonInput=data
        )

        log_print(url=test_base + logout_urlp, method='GET', response=self.r)
        print('logout success' if eval(self.r.text)['status'] == 'NOT_LOGIN' else 'logout error') # str to dict using func eval
        print('\n')