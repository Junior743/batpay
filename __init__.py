from pyramid.config import Configurator
from wsgiref.simple_server import make_server


class BatPay(object):
    '''
    BAT PAY - Aplicação de gerenciamento de recursos
    '''

    ROTAS = [
        {"nome":"usuarios", "uri":"/usuarios"}, 
        {"nome":"usuario", "uri":"/usuarios/{codigo}"}, 
        {"nome":"planilhas", "uri":"/planilhas"}, 
        {"nome":"planilha", "uri":"/planilha/{codigo}"}, 
        {"nome":"relatorios", "uri":"/relatorios"}, 
        {"nome":"relatorio", "uri":"/relatorio/{codigo}"}, 
        {"nome":"relatorios_detalhados", "uri":"/relatorios/{codigo}/detalhados"}
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
