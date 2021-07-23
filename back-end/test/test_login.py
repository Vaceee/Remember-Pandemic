import ddt
import unittest
from baseOp import request_return, log_print, test_base

# due to unittest execute order(by "class name"), so named as 'test01...','test02...'

#-------------------------url block--------------------------#
login_urlp = 'login'
logout_urlp = 'logout'

#-------------------------test sets--------------------------#
test_data_login = [
    {'usr_no':'1859999', 'usr_password':'password'}
]

#-----------------------test segment--------------------------#
@ddt.ddt
class test01_login(unittest.TestCase):

    # construct test env
    # only execute once when test begins
    @classmethod
    def setUpClass(cls):
        cls.base_url = test_base
        cls.login_urlp = login_urlp
        cls.url = cls.base_url + cls.login_urlp
        cls.r = None

    # url: /login
    # login and generate cookies
    @ddt.data(*test_data_login)
    def test_1(self, data):
        self.r = request_return(
            url=self.url,
            method='POST',
            jsonInput=data
        )
        # test01_login. means global variable
        log_print(url=self.url, method='POST', response=self.r)

    # url: /login
    # get msg of user
    def test_2(self):
        self.r = request_return(
            url=self.url,
            method='GET'
        )
        log_print(url=self.url, method='GET', response=self.r)

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