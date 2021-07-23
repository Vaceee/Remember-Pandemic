import unittest
import ddt
from baseOp import request_return, log_print, test_base

#-------------------------url block--------------------------#
login_urlp = 'login'
sections_fetch_urlp = 'sections/fetch'
logout_urlp = 'logout'

#-------------------------test sets--------------------------#
test_data_login = [
    {'usr_no':'1859999', 'usr_password':'password'}
]

#-----------------------test segment--------------------------#
@ddt.ddt
class test02_sections(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = test_base
        cls.sections_fecth_urlp = sections_fetch_urlp
        cls.login_urlp = login_urlp
        cls.url = cls.base_url + cls.sections_fecth_urlp
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

    # url: /sections/fetch
    # to fetch all sections
    def test_1(self):
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