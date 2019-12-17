import unittest
from django.test import TestCase
from django.urls import reverse
from django.test import Client

class Test(unittest.TestCase):
    @classmethod
    def startUpClass(cls):
        pass 

    @classmethod
    def takeDownClass(cls):
        pass 

    # startup and takedown
    def startUp(self):
        pass

    def takeDown(self):
        pass
    
    def runTest(self):
        pass

c = Client()
# views 
def test_get_routes(self):
    # Homepage
        response = c.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200)
     # products
        response = c.get('/products', content_type="html/text")
        self.assertEqual(response.status_code, 200)
    # work
        response = c.get('/work', content_type="html/text")
        self.assertEqual(response.status_code, 200)
    # about
        response = c.get('/about', content_type="html/text")
        self.assertEqual(response.status_code, 200)
    # news
        response = c.get('/news', content_type="html/text")
        self.assertEqual(response.status_code, 200)
    # cart
        response = c.get('/cart', content_type="html/text")
        self.assertEqual(response.status_code, 200)
    # register
        response = c.get('/register', content_type="html/text")
        self.assertEqual(response.status_code, 200)
    # Login
        response = c.get('/login', content_type="html/text")
        self.assertEqual(response.status_code, 200)
        
def test_get_routes_connect_template(self):
    # Homepage
        response = c.get('/', content_type="html/text")
        self.assertTrue(b'Noir Digital Graphic Design' in response.data)
    # work
        response = c.get('/work', content_type="html/text")
        self.assertTrue(b'Previous Work' in response.data)
    # about
        response = c.get('/about', content_type="html/text")
        self.assertTrue(b'About Noir Digital' in response.data)
    # news
        response = c.get('/news', content_type="html/text")
        self.assertTrue(b'Noir Digital News' in response.data)
    # register
        response = c.get('/register', content_type="html/text")
        self.assertTrue(b'Create a new account' in response.data)
    # Login
        response = c.get('/login', content_type="html/text")
        self.assertTrue(b'Login' in response.data)
        
if __name__ == "__main__":
    unittest.main()