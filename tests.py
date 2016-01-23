from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that login pg loads with text expected
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(('Please login'.encode('utf-8')) in response.data)

    #ensure login behaves correctly w correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
        	'/login', 
        	data =dict(username = "admin", password ="admin"),
        	follow_redirects =True)
        self.assertIn(('you were just logged in'.encode('utf-8')), response.data)

    #ensure login works right w incorrect credentials

    #ensure logout works right
if __name__ == '__main__':
    unittest.main()