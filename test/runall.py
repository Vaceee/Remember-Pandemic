import unittest
import ddt
import sys
from BeautifulReport import BeautifulReport
import test_login, test_sections, test_posts, test_replies, test_logout
import test_messages, test_notices, test_search, test_profile

if __name__ == "__main__":

    suite = unittest.TestSuite()


    if 'login' in sys.argv or '--all' in sys.argv:
        print('/login test added')
        login_tests = unittest.TestLoader().loadTestsFromTestCase(
            testCaseClass=test_login.test01_login
        )
        suite.addTests(login_tests)

    if 'sections' in sys.argv or '--all' in sys.argv:
        print('/sections test added')
        sections_tests = unittest.TestLoader().loadTestsFromTestCase(
            testCaseClass=test_sections.test02_sections
        )
        suite.addTests(sections_tests)

    if 'posts' in sys.argv or '--all' in sys.argv:
        print('/posts test added')
        posts_tests = unittest.TestLoader().loadTestsFromTestCase(
            testCaseClass=test_posts.test03_posts
        )
        suite.addTests(posts_tests)

    if 'replies' in sys.argv or '--all' in sys.argv:
        print('/replies test added')
        replies_tests = unittest.TestLoader().loadTestsFromTestCase(
            testCaseClass=test_replies.test04_replies
        )
        suite.addTests(replies_tests)

    if 'messages' in sys.argv or '--all' in sys.argv:
        print('/messages test added')
        messages_tests = unittest.TestLoader().loadTestsFromTestCase(
            testCaseClass=test_messages.test05_messages
        )
        suite.addTests(messages_tests)

    if 'notices' in sys.argv or '--all' in sys.argv:
        print('/notices test added')
        notices_tests = unittest.TestLoader().loadTestsFromTestCase(
            testCaseClass=test_notices.test06_notices
        )
        suite.addTests(notices_tests)

    if 'profile' in sys.argv or '--all' in sys.argv:
        print('/profile test added')
        profile_tests = unittest.TestLoader().loadTestsFromTestCase(
            testCaseClass=test_profile.test07_profile
        )
        suite.addTests(profile_tests)

    if 'search' in sys.argv or '--all' in sys.argv:
        print('/search test added')
        search_tests = unittest.TestLoader().loadTestsFromTestCase(
            testCaseClass=test_search.test07_search
        )
        suite.addTests(search_tests)

    if 'logout' in sys.argv or '--all' in sys.argv:
        print('/logout test added')
        logout_tests = unittest.TestLoader().loadTestsFromTestCase(
            testCaseClass=test_logout.test99_logout
        )
        suite.addTests(logout_tests)


    runner = unittest.TextTestRunner(verbosity=2)
    res = BeautifulReport(suite)
    res.report(filename='test', description='test Beauty')
