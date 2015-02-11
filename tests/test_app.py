import unittest
import urllib2

class TestWebService(unittest.TestCase):

#    def setUp(self):
#        print os.basedir
#        print os.path

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
