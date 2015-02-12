import unittest
import urllib2
from app.SampleApp import app


class TestWebService(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
#        print os.basedir
#        print os.path

    def test_service_name_incorrect(self):
        with open('BgTest.xml') as source_data:
            soap_body = source_data.read()
        headers = {'Content-Type': 'text/xml'}
        response = self.app.post('/soap/nosuchservice', data = soap_body, headers = headers)
        self.assertEqual(response.status, '404 NOT FOUND')

    def test_service_with_good_xml_data(self):
        with open('BgTest.xml') as source_data:
            soap_body = source_data.read()
        headers = {'Content-Type': 'text/xml'}
        response = self.app.post('/soap/bgservice/reflection', data = soap_body, headers = headers)
        self.assertEqual(response.status, '200 OK')

    def test_service_with_bad_xml_data(self):
        with open('BgBad.xml') as source_data:
            soap_body = source_data.read()
        headers = {'Content-Type': 'text/xml'}
        response = self.app.post('/soap/bgservice/reflection', data = soap_body, headers = headers)
        self.assertEqual(response.status, '500 Internal Server Error')


    def test_reflection(self):
        with open('BgTest.xml') as source_data:
            soap_body = source_data.read()
        req = urllib2.Request(url='http://localhost:5000/soap/bgservice/reflection', data=soap_body)
        req.add_header('Content-Type', 'text/xml')
        resp = urllib2.urlopen(req)
        content = resp.read()
        self.assertIn('TN0001', content)

    def test_reflection_malformed_request(self):
        with open('BgBad.xml') as source_data:
            soap_body = source_data.read()
        req = urllib2.Request(url='http://localhost:5000/soap/bgservice/reflection', data=soap_body)
        req.add_header('Content-Type', 'text/xml')
        self.assertRaises(urllib2.HTTPError, urllib2.urlopen, req)
