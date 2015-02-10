import logging
from suds.client import Client as SudsClient

# Send log messages to console
logging.basicConfig(level=logging.INFO)
# Set Suds logging level to debug, outputs the SOAP messages.
logging.getLogger('suds.client').setLevel(logging.DEBUG)


url = 'http://127.0.0.1:5000/soap/someservice?wsdl'
client = SudsClient(url=url, cache=None)
r = client.service.echo(str='hello world', cnt=3)
print r
