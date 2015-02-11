from flask import Flask
from flask.ext.spyne import Spyne
from spyne.protocol.soap import Soap11
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable

app = Flask(__name__)
spyne = Spyne(app)

class BgSoapService(spyne.Service):
    __service_url_path__ = '/soap/bgservice/reflection'
    __in_protocol__ = Soap11(validator='lxml')
    __out_protocol__ = Soap11()

    @spyne.srpc(Unicode, Unicode, Unicode, Integer, _returns=Iterable(Unicode))
    def bg(title, address, application, id):

        yield title
        yield address
        yield application
        yield str(id)

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
