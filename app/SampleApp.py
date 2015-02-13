from flask import Flask
from flask.ext.spyne import Spyne
from spyne.protocol.soap import Soap11
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable
from random import randint

app = Flask(__name__)
spyne = Spyne(app)

class BgSoapService(spyne.Service):
    __service_url_path__ = '/soap/bgservice'
    __in_protocol__ = Soap11(validator='lxml')
    __out_protocol__ = Soap11()

    @spyne.srpc(Unicode, Unicode, Unicode, Integer, _returns=Iterable(Unicode))
    def reflection(title, address, application, id):

        yield title
        yield address
        yield application
        yield str(id)

    @spyne.srpc(Unicode, Unicode, Unicode, _returns=Unicode)
    def tran(title, address, application):
        static_id = randint(0,100)
        return str(static_id)

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
