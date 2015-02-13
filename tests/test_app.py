import unittest
from app.SampleApp import app

REFLECTION_SVC_ENDPOINT = '/soap/bgservice/reflection'
TRAN_SVC_ENDPOINT = '/soap/bgservice/tran'

GOOD_REFLECTION_REQ_DATA = '''<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="tns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Header/>
   <ns0:Body>
      <ns1:reflection>
         <ns1:title>TN0001</ns1:title>
         <ns1:address>8 Cornwall Street Plymouth PL6 7FD</ns1:address>
         <ns1:application>AP1</ns1:application>
         <ns1:id>3</ns1:id>
      </ns1:reflection>
   </ns0:Body>
</SOAP-ENV:Envelope>'''

BAD_REFLECTION_REQ_DATA = '''<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="tns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Header/>
   <ns0:Body>
      <ns1:reflection>
         <ns1:title>TN0001</ns1:title>
         <ns1:address>8 Cornwall Street Plymouth PL6 7FD</ns1:address>
         <ns1:application>AP1</ns1:application>
         <ns1:id>THREE</ns1:id>
      </ns1:reflection>
   </ns0:Body>
</SOAP-ENV:Envelope>'''

GOOD_TRAN_REQ_DATA = '''<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="tns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Header/>
   <ns0:Body>
      <ns1:tran>
         <ns1:title>TN0001</ns1:title>
         <ns1:address>8 Cornwall Street Plymouth PL6 7FD</ns1:address>
         <ns1:application>AP1</ns1:application>
      </ns1:tran>
   </ns0:Body>
</SOAP-ENV:Envelope>'''


class TestWebService(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    # Test that a request to an unknown service elicits a 404 error
    def test_service_name_incorrect(self):
        response = self.service_function('/soap/nosuchservice', GOOD_REFLECTION_REQ_DATA)
        self.assertEqual(response.status, '404 NOT FOUND')

    # Test that a reflection service request with valid structure is accepted by the service
    def test_reflection_service_status_with_good_xml_data(self):
        response = self.service_function(REFLECTION_SVC_ENDPOINT, GOOD_REFLECTION_REQ_DATA)
        self.assertEqual(response.status, '200 OK')

    # Test that the response from the reflection service contains the correct data - needs
    # expansion and maybe further checks once the happy path response is agreed
    def test_reflection_service_response_with_good_xml_data(self):
        response = self.service_function(REFLECTION_SVC_ENDPOINT, GOOD_REFLECTION_REQ_DATA)
        self.assertIn('TN0001', response.get_data())

    # Test that a reflection service request with invalid data type elicits a 500 error
    def test_relection_service_status_with_bad_xml_data(self):
        response = self.service_function(REFLECTION_SVC_ENDPOINT, BAD_REFLECTION_REQ_DATA)
        self.assertEqual(response.status, '500 Internal Server Error')

    # Test that a reflection service request with invalid data type elicits a SOAP fault response
    def test_reflection_service_response_with_bad_xml_data(self):
        response = self.service_function(REFLECTION_SVC_ENDPOINT, BAD_REFLECTION_REQ_DATA)
        self.assertIn('SchemaValidationError', response.get_data())

    # Test that a tran service request with valid structure is accepted by the service
    def test_tran_service_response_with_good_xml_data(self):
        response = self.service_function(TRAN_SVC_ENDPOINT, GOOD_TRAN_REQ_DATA)
        self.assertEqual(response.status, '200 OK')

    # TODO - Test that a tran service response returns a valid identifier between 0 and 100

    def service_function(self, service_endpoint, service_data):
        soap_body = service_data
        headers = {'Content-Type': 'text/xml'}
        response = self.app.post(service_endpoint, data = soap_body, headers = headers)
        return response
