import ddt
import unittest
from baseOp import request_return, log_print, test_base

#-------------------------url block--------------------------#
login_urlp = 'login'
logout_urlp = 'logout'

#-------------------------test sets--------------------------#
test_data_login = [
    {'usr_no':'1859999', 'usr_password':'password'}
]

#-----------------------test segment--------------------------#
@ddt.ddt
class test99_logout(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = test_base
        cls.logout_urlp = logout_urlp
        cls.login_urlp = login_urlp
        cls.url = cls.base_url + cls.logout_urlp
        cls.r = None

    # url: /login
    # generate cookies
    @ddt.data(*test_data_login)
    def test_0(self, data):
        self.r = request_return(
            url=self.base_url + self.login_urlp,
            method='POST',
            jsonInput=data
        )

    # url: /logout
    # delete cookies while teardown
    def test_1(self):
        self.r = request_return(
            url=self.url,
            method='GET'
        )

        log_print(url=self.url, method='GET', response=self.r)
        print('logout success' if eval(self.r.text)['status'] == 'GET_SUCCESS' else 'logout error') # str to dict using func eval
        print('\n')