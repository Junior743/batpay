from pyramid.config import Configurator
from wsgiref.simple_server import make_server


class BatPay(object):
    '''
    BAT PAY - Application for management of apportionments.
    '''

    ROTAS = [
        {"nome":"authentication", "uri":"/authentication"}, 
        {"nome":"users", "uri":"/users"}, 
        {"nome":"user", "uri":"/users/{code}"}, 
        {"nome":"spreadsheets", "uri":"/spreadsheets"}, 
        {"nome":"spreadsheet", "uri":"/spreadsheets/{code}"}, 
        {"nome":"reports", "uri":"/reports"}, 
        {"nome":"report", "uri":"/reports/{code}"}, 
        {"nome":"detailed-reports", "uri":"/reports/{code}/detailed-reports"}
    ]

    @classmethod
    def servir(cls):
        with Configurator() as config:
            cls.configurar_rotas(config)
            app = config.make_wsgi_app()
        print("Construindo servidor em 0.0.0.0:8080")
        server = make_server('0.0.0.0', 8080, app)
        print("Concluido!")
        server.serve_forever()

    @classmethod
    def configurar_rotas(cls, config):
        for _rota in cls.ROTAS:
            config.add_route(_rota["nome"], _rota["uri"])

if __name__ == "__main__":
    BatPay.servir()
