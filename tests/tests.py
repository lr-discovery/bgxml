import unittest
import urllib2
from app import SampleApp
from app.SampleApp import app

class TestWebService(unittest.TestCase):

    def setUp(self):
        self.app = SampleApp.app.test_client()

    def test_echo(self):
        with open('test.xml') as source_data:
            soap_body = source_data.read()
        req = urllib2.Request(url='http://localhost:5000/soap/someservice/echo', data=soap_body)
        req.add_header('Content-Type', 'text/xml')
        resp = urllib2.urlopen(req)
        content = resp.read()
        self.assertIn('hello world', content)

    def test_echo_with_malformed_data(self):
        with open('bad.xml') as source_data:
            soap_body = source_data.read()
        req = urllib2.Request(url='http://localhost:5000/soap/someservice/echo', data=soap_body)
        req.add_header('Content-Type', 'text/xml')
        resp = urllib2.urlopen(req)
        content = resp.read()
        self.assertIn('BAD', content)

if __name__ == '__main__':
    unittest.main()
