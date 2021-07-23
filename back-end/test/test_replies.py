import ddt
import unittest
from baseOp import request_return, log_print, test_base

#-------------------------url block--------------------------#
login_urlp = 'login'
replies_fetch_urlp = 'replies/fetch'
replies_new_urlp = 'replies/new'
replies_edit_urlp = 'replies/edit'
replies_delete_urlp = 'replies/delete'
replies_like_urlp = 'replies/like'
logout_urlp = 'logout'

#-------------------------test sets--------------------------#
test_data_login = [
    {'usr_no':'1859999', 'usr_password':'password'}
]
test_data_replies_fetch = [
    {'post_id': 1, 'reply_id':-1, 'page': 1, 'limit': 10},
    {'post_id': 2, 'reply_id':-1, 'page': 1, 'limit': 10},
    {'post_id': 1, 'reply_id':1, 'page': 1, 'limit': 5},
]
test_data_replies_launch = [
    {
        'content'   : 'aoligei!',
        'post_id'   : 1,
        'rep_to'    : -1,
    },
    {
        'content'   : '您就是冬泳怪鸽？',
        'post_id'   : 1,
        'rep_to'    : 1,
    },
    {
        'content'   : 'eat mihotel',
        'post_id'   : 1,
        'rep_to'    : 1,
    },
    {
        'content'   : 'meizhierzhier',
        'post_id'   : 1,
        'rep_to'    : 3,
    },
    {
        'content'   : '社会主义好',
        'post_id'   : 2,
        'rep_to'    : -1,
    }
]
test_data_replies_edit = [
    {
        'id'        : 1,
        'content'   : 'yigeilo!'
    }
]
test_data_replies_delete = [
    {'id' : 1}
]
test_data_replies_like = [
    {'rep_id' : 1, 'method' : 'like'},
    {'rep_id' : 1, 'method' : 'cancel'}
]

#-----------------------test segment--------------------------#
@ddt.ddt
class test04_replies(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = test_base
        cls.replies_fetch_urlp = replies_fetch_urlp
        cls.replies_new_urlp = replies_new_urlp
        cls.replies_edit_urlp = replies_edit_urlp
        cls.replies_delete_urlp = replies_delete_urlp
        cls.replies_like_urlp = replies_like_urlp
        cls.r = None

    # url: /login
    # to yield cookies
    @ddt.data(*test_data_login)
    def test_0(self, data):
        self.r = request_return(
            url=test_base + login_urlp,
            method='POST',
            jsonInput=data
        )


    # url: /replies/new
    # launch posts
    #@unittest.skip
    @ddt.data(*test_data_replies_launch)
    def test_1(self, data):
        self.r = request_return(
            url=self.base_url + self.replies_new_urlp,
            method='POST',
            jsonInput=data
        )
        log_print(
            url=self.base_url + self.replies_new_urlp,
            method='POST',
            response=self.r
        )


    # url: /replies/fetch
    # fetch replies
    #@unittest.skip
    @ddt.data(*test_data_replies_fetch)
    def test_2(self, data):
        self.r = request_return(
            url=self.base_url + self.replies_fetch_urlp,
            method='GET',
            parameInput=data
        )
        log_print(
            url=self.base_url + self.replies_fetch_urlp,
            method='GET',
            response=self.r
        )


    # url: /replies/edit
    # edit replies
    #@unittest.skip
    @ddt.data(*test_data_replies_edit)
    def test_3(self, data):
        self.r = request_return(
            url=self.base_url + self.replies_edit_urlp,
            method='POST',
            jsonInput=data
        )
        log_print(
            url=self.base_url + self.replies_edit_urlp,
            method='POST',
            response=self.r
        )

    # url: /replies/like
    # like/cancel replies
    #@unittest.skip
    @ddt.data(*test_data_replies_like)
    def test_4(self, data):
        self.r = request_return(
            url=self.base_url + self.replies_like_urlp,
            method='POST',
            jsonInput=data
        )
        log_print(
            url=self.base_url + self.replies_like_urlp,
            method='POST',
            response=self.r
        )


    # url: /replies/delete
    # delete replies
    #@unittest.skip
    @ddt.data(*test_data_replies_delete)
    def test_5(self, data):
        self.r = request_return(
            url=self.base_url + self.replies_delete_urlp,
            method='POST',
            jsonInput=data
        )
        log_print(
            url=self.base_url + self.replies_delete_urlp,
            method='POST',
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