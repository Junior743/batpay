from pyramid.config import Configurator
from wsgiref.simple_server import make_server

# import views
from batpay.views import (
    ViewAdministrator,
    ViewManager
)


class Main(object):
    '''
    BAT PAY - Application for management of apportionments.
    '''

    ROTAS = [
        {"name":"authentication", "uri":"/authentication"}, 
        {"name":"users", "uri":"/users"}, 
        {"name":"user", "uri":"/users/{code}"}, 
        {"name":"spreadsheets", "uri":"/spreadsheets"}, 
        {"name":"spreadsheet", "uri":"/spreadsheets/{code}"}, 
        {"name":"expenses-reports", "uri":"/reports/{code}/expenses-reports"}
    ]

    VIEWS = [
        {"view":ViewAdministrator.extract_expenses_reports, "route_name":"expenses-reports", "request_method":"GET"}, 
        {"view":ViewManager.add_users, "route_name":"users", "request_method":"POST"}, 
        {"view":ViewManager.update_users, "route_name":"user", "request_method":"PUT"}, 
        {"view":ViewManager.delete_users, "route_name":"user", "request_method":"DELETE"}, 
        {"view":ViewManager.get_users, "route_name":"user", "request_method":"GET"}
    ]

    @classmethod
    def servir(cls):
        with Configurator() as config:
            cls.config_routes(config)
            cls.config_views(config)
            # config.scan(views)
            app = config.make_wsgi_app()

        print("Construindo servidor em 0.0.0.0:8080")
        server = make_server('0.0.0.0', 8080, app)
        print("Concluido!")
        server.serve_forever()

    @classmethod
    def config_routes(cls, config):
        for _rota in cls.ROTAS:
            config.add_route(_rota["name"], _rota["uri"])

    @classmethod
    def config_views(cls, config):
        for _view in cls.VIEWS:
            config.add_view(
                _view["view"], 
                route_name=_view["route_name"], 
                request_method=_view["request_method"]
            )


if __name__ == "__main__":
    Main.servir()
