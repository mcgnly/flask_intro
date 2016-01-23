from app import app
import unittest


class FlaskTestCase(unittest.TestCase):
#NOTE: all the tests have to start with the word "test_" or else the tester won't find it

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200) #does page load successfully?

    # Ensure that login pg loads with text expected
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(('Please login'.encode('utf-8')) in response.data) #have to add the .encode('utf-8') step because of weirdness in py2 vs py3

    #ensure login behaves correctly w correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
        	'/login', 
        	data =dict(username = "admin", password ="admin"),
        	follow_redirects =True) #have to follow redirects to get flash messages
        self.assertIn(('you were just logged in'.encode('utf-8')), response.data)

    #ensure login works right w incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
        	'/login', 
        	data =dict(username = "notadmin", password ="notadmin"),
        	follow_redirects =True)
        self.assertIn(('Invalid Credentials. Please try again.'.encode('utf-8')), response.data)

    #ensure logout works right
    def test_logout_page_loads(self):
        tester = app.test_client(self)
        #first we have to log in, to test logout
        response = tester.post(
        	'/login', 
        	data =dict(username = "admin", password ="admin"),
        	follow_redirects =True)
        #now that we're in, we can test geting out
        response = tester.get('/logout', follow_redirects=True)
        self.assertTrue(('you logged out'.encode('utf-8')) in response.data) #have to add the .encode('utf-8') step because of weirdness in py2 vs py3

    #check that you have to be logged in to get to the main page
    def test_logged_in_before_main(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertTrue(('You need to login first.'.encode('utf-8')) in response.data)

    #check that posts appear on the main page
    	#create a test database
    	#add data to it
    	#check that it worked


if __name__ == '__main__':
    unittest.main()