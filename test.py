import unittest
from flask import url_for, request
from flask_testing import TestCase
from app import app_factory

class TestHello(TestCase):

    def create_app(self):
        app = app_factory(debug=True)
        app.config['TESTING'] = True
        return app
     
    def setUp(self):
        pass
 
    def tearDown(self):
        pass
        
    def test_hello_no_names(self):
        _path = url_for('demotest', demo_test_value='Mehmet')
        response = self.client.get(_path)
        self.assertIn(b'Mehmet', response.data)
       
    # We can test the main page against its main
    # header, which is 'Product Database' at the moment
    def test_product_listing_main_page(self):
        _path = url_for('index')
        response = self.client.get(_path)
        self.assertIn(b'Product Database', response.data)    

    # We can test the main page against db content
    # since main page lists database content
    def test_product_listing_main_pageby_db_content(self):
        _path = url_for('index')
        response = self.client.get(_path)
        self.assertIn(b'Nintendo DS Lite', response.data)    

    # Page element may be Name, Price, Category or something 
    # similar that you see on the main page
    def test_product_listing_main_pageby_a_page_element(self):
        _path = url_for('index')
        response = self.client.get(_path)
        self.assertIn(b'Price', response.data)    
        
if __name__ == '__main__':
    unittest.main()
