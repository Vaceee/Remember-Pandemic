import unittest
import ddt
from baseOp import request_return, log_print, test_base

#-------------------------url block--------------------------#
login_urlp = 'login'
notices_send_urlp = 'notices/send'
notices_list_urlp = 'notices/list'
notices_detail_urlp = 'notices/detail'
logout_urlp = 'logout'

#-------------------------test sets--------------------------#
test_data_login = [
    {
        'usr_no': '1859999',
        'usr_password': 'password',
    }
]
test_data_notices_send = [
    {
        'content': 'sjnb!',
        'bas_id': 1,
    }
]
test_data_notices_detail = [
    {
        'bas_id': 1,
    }
]

#-----------------------test segment--------------------------#
@ddt.ddt
class test06_notices(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = test_base
        cls.notices_send_urlp = notices_send_urlp
        cls.notices_list_urlp = notices_list_urlp
        cls.notices_detail_urlp = notices_detail_urlp
        cls.login_urlp = login_urlp
        cls.r = None

    # url: /login
    # to yield cookies
    @ddt.data(*test_data_login)
    def test_0(self, data):
        self.r = request_return(
            url=self.base_url + self.login_urlp,
            method='POST',
            jsonInput=data
        )

    # url: /notices/send
    # to send a notice
    @ddt.data(*test_data_notices_send)
    def test_1(self, data):
        self.r = request_return(
            url=self.base_url + self.notices_send_urlp,
            method='POST',
            jsonInput=data
        )
        log_print(
            url=self.base_url + self.notices_send_urlp,
            method='GET',
            response=self.r
        )

    # url: /notices/list
    # to list all notices about a user
    def test_2(self):
        self.r = request_return(
            url=self.base_url + self.notices_list_urlp,
            method='GET'
        )
        log_print(
            url=self.base_url + self.notices_list_urlp,
            method='GET',
            response=self.r
        )

    # url: /notices/detail
    # to show details of notices
    @ddt.data(*test_data_notices_detail)
    def test_3(self, data):
        self.r = request_return(
            url=self.base_url + self.notices_detail_urlp,
            method='GET',
            jsonInput=data
        )
        log_print(
            url=self.base_url + self.notices_detail_urlp,
            method='GET',
            response=self.r
        )


    # url: /logout
    # destruct env and delete cookies
    # it should be a cls. cls and ddt cannot coexist however
    def test_99(self):
        self.r = request_return(
            url=test_base + logout_urlp,
            method='GET'
        )
        print('logout success' if eval(self.r.text)['status'] == 'GET_SUCCESS' else 'logout error') # str to dict using func eval
        print('\n')