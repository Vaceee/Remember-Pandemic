import unittest
import ddt
from baseOp import request_return, log_print, test_base

#-------------------------url block--------------------------#
login_urlp = 'login'
messages_send_urlp = 'messages/send'
messages_list_urlp = 'messages/list'
messages_chat_urlp = 'messages/chat'
logout_urlp = 'logout'

#-------------------------test sets--------------------------#
test_data_login = [
    {
        'usr_no': '1859999',
        'usr_password': 'password'
    }
]
test_data_messages_send = [
    {
        'usr_to': '2',
        'content': 'sjnb!'
    }
]
test_data_messages_chat = [
    {
        'usr_to': 2,
    }
]

#-----------------------test segment--------------------------#
@ddt.ddt
class test05_messages(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = test_base
        cls.messages_send_urlp = messages_send_urlp
        cls.messages_list_urlp = messages_list_urlp
        cls.messages_chat_urlp = messages_chat_urlp
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

    # url: /messages/send
    # to send a message
    @ddt.data(*test_data_messages_send)
    def test_1(self, data):
        self.r = request_return(
            url= self.base_url + self.messages_send_urlp,
            method='POST',
            jsonInput=data
        )
        log_print(
            url=self.base_url + self.messages_send_urlp,
            method='GET',
            response=self.r
        )

    # url: /messages/list
    # to list all messages of a user
    def test_2(self):
        self.r = request_return(
            url= self.base_url + self.messages_list_urlp,
            method='GET'
        )
        log_print(
            url=self.base_url + self.messages_list_urlp,
            method='GET',
            response=self.r
        )

    # url: /messages/chat
    # to send a message
    @ddt.data(*test_data_messages_chat)
    def test_3(self, data):
        self.r = request_return(
            url= self.base_url + self.messages_chat_urlp,
            method='GET',
            jsonInput=data
        )
        log_print(
            url=self.base_url + self.messages_chat_urlp,
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