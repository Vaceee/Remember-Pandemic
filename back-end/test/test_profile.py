import ddt
import unittest
from baseOp import request_return, log_print, test_base

# due to unittest execute order(by "class name"), so named as 'test01...','test02...'

#-------------------------url block--------------------------#
login_urlp = 'login'
setpassword_urlp = 'profile/setpassword'
logout_urlp = 'logout'

#-------------------------test sets--------------------------#
test_data_login = [
    {'usr_no':'1859999', 'usr_password':'password'}
]
test_data_setpassword = [
    {'password':'iamgod'}
]
test_data_login2 = [
    {'usr_no':'1859999', 'usr_password':'iamgod'}
]
test_data_setpassword2 = [
    {'password': 'password'}
]


#-----------------------test segment--------------------------#
@ddt.ddt
class test07_profile(unittest.TestCase):

    # construct test env
    # only execute once when test begins
    @classmethod
    def setUpClass(cls):
        cls.base_url = test_base
        cls.login_urlp = login_urlp
        cls.setpassword_urlp = setpassword_urlp
        cls.logout_urlp = logout_urlp
        cls.r = None

    # url: /login
    # login and generate jwt
    @ddt.data(*test_data_login)
    def test_1(self, data):
        self.r = request_return(
            url=self.base_url + self.login_urlp,
            method='POST',
            jsonInput=data
        )
        # test01_login. means global variable
        log_print(
            url=self.base_url + self.login_urlp,
            method='POST',
            response=self.r
        )

    # url: /profile/setpassword
    # reset password and delete jwt
    @ddt.data(*test_data_setpassword)
    def test_2(self, data):
        self.r = request_return(
            url=self.base_url + self.setpassword_urlp,
            method='POST',
            jsonInput=data
        )
        log_print(
            url=self.base_url + self.setpassword_urlp,
            method='POST',
            response=self.r
        )

    # url: /login
    # login and generate jwt
    @ddt.data(*test_data_login2)
    def test_3(self, data):
        self.r = request_return(
            url=self.base_url + self.login_urlp,
            method='POST',
            jsonInput=data
        )
        # test01_login. means global variable
        log_print(
            url=self.base_url + self.login_urlp,
            method='POST',
            response=self.r
        )


    # url: /profile/setpassword
    # reset password and delete jwt
    @ddt.data(*test_data_setpassword2)
    def test_4(self, data):
        self.r = request_return(
            url=self.base_url + self.setpassword_urlp,
            method='POST',
            jsonInput=data
        )
        log_print(
            url=self.base_url + self.setpassword_urlp,
            method='POST',
            response=self.r
        )


    # url: /login
    # login and generate jwt
    @ddt.data(*test_data_login)
    def test_5(self, data):
        self.r = request_return(
            url=self.base_url + self.login_urlp,
            method='POST',
            jsonInput=data
        )
        # test01_login. means global variable
        log_print(
            url=self.base_url + self.login_urlp,
            method='POST',
            response=self.r
        )


    # url: /logout
    # destruct env and delete cookies
    # it should be a cls. cls and ddt cannot coexist however
    def test_99(self):
        self.r = request_return(
            url=self.base_url + self.logout_urlp,
            method='GET'
        )
        print('logout success' if eval(self.r.text)['status'] == 'GET_SUCCESS' else 'logout error') # str to dict using func eval
        print('\n')