import ddt
import unittest
from baseOp import request_return, log_print, test_base

#-------------------------url block--------------------------#
login_urlp = 'login'
posts_fetch_urlp = 'posts/fetch'
posts_new_urlp = 'posts/new'
posts_edit_urlp = 'posts/edit'
posts_delete_urlp = 'posts/delete'
posts_fetch_one_urlp = 'posts/fetch-one'
posts_merge_urlp = 'posts/merge'
logout_urlp = 'logout'

#-------------------------test sets--------------------------#
test_data_login = [
    {'usr_no':'1859999', 'usr_password':'password'}
]
test_data_posts_fetch = [
    {'page': 1, 'limit': 1, 'bas_id': 1},
    {'page': 1, 'limit': 1, 'bas_id': 2}
]
test_data_posts_launch = [
    {
        'title'     : 'lphnb!',
        'content'   : 'lphnblphnblphnb!',
        'bas_id'    : '2',
        'img'       : None
    }
]
test_data_posts_edit = [
    {
        'id'        : 1,	#reasonbility of whether a post_id could be sent by client is uncertain
		'title'     : 'ljgnb!',
        'content'   : 'lphnblphnbljgnb!',
        'bas_id'    : '2',
        'img'       : None
    }
]
test_data_posts_delete = [
    {'id' : 4}
]
test_data_posts_fetch_one = [
	{'post_id' : 1}
]
test_data_posts_merge = [
	{'merge_from' : 1, 'merge_to' : 2}
]

#-----------------------test segment--------------------------#
@ddt.ddt
class test03_posts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = test_base
        cls.login_urlp = login_urlp
        cls.posts_fetch_urlp = posts_fetch_urlp
        cls.posts_fetch_one_urlp = posts_fetch_one_urlp
        cls.posts_new_urlp = posts_new_urlp
        cls.posts_edit_urlp = posts_edit_urlp
        cls.posts_delete_urlp = posts_delete_urlp
        cls.posts_merge_urlp = posts_merge_urlp
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

    # url: /posts/fetch
    # test fetch all
    #@unittest.skip
    @ddt.data(*test_data_posts_fetch)
    def test_1(self, data):
        self.r = request_return(
            url=self.base_url + self.posts_fetch_urlp,
            method='GET',
            parameInput=data
        )
        log_print(
            url=self.base_url + self.posts_fetch_urlp,
            method='GET',
            response=self.r
        )

    # url: /posts/new
    # launch posts
    #@unittest.skip
    @ddt.data(*test_data_posts_launch)
    def test_2(self, data):
        self.r = request_return(
            url=self.base_url + self.posts_new_urlp,
            method='POST',
            jsonInput=data
        )
        log_print(
            url=self.base_url + self.posts_new_urlp,
            method='POST',
            response=self.r
        )

    # url: /posts/edit
    # edit posts
    #@unittest.skip
    @ddt.data(*test_data_posts_edit)
    def test_3(self, data):
        self.r = request_return(
            url=self.base_url + self.posts_edit_urlp,
            method='POST',
            jsonInput=data
        )
        log_print(
            url=self.base_url + self.posts_edit_urlp,
            method='POST',
            response=self.r
        )

    # url: /posts/delete
    # delete posts
    #@unittest.skip
    @ddt.data(*test_data_posts_delete)
    def test_4(self, data):
        self.r = request_return(
            url=self.base_url + self.posts_delete_urlp,
            method='POST',
            jsonInput=data
        )
        log_print(
            url=self.base_url + self.posts_delete_urlp,
            method='POST',
            response=self.r
        )

    # url: /posts/fetch-one
    # test fetch one post
    #@unittest.skip
    @ddt.data(*test_data_posts_fetch_one)
    def test_5(self, data):
        self.r = request_return(
            url=self.base_url + self.posts_fetch_one_urlp,
            method='GET',
            parameInput=data
        )
        log_print(
            url=self.base_url + self.posts_fetch_one_urlp,
            method='GET',
            response=self.r
        )

    # url: /posts/merge
    # merge posts
    #@unittest.skip
    @ddt.data(*test_data_posts_merge)
    def test_6(self, data):
        self.r = request_return(
            url=self.base_url + self.posts_merge_urlp,
            method='POST',  #adminRequired
            jsonInput=data
        )
        log_print(
            url=self.base_url + self.posts_merge_urlp,
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