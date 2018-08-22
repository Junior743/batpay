from pyramid.view import view_config
from pyramid.response import Response

from oauth2 import view_authenticate


class ViewBase(object):
    pass

class ViewAdministrator(ViewBase):

    # @view_config(
    #     route_name="reports", 
    #     request_method="GET", 
    #     renderer="json"
    # )
    @staticmethod
    @view_authenticate
    def extract_reports(context, request, sessao):
        import ipdb; ipdb.set_trace()
        _result = sessao.get("https://secure.splitwise.com/api/v3.0/get_groups")
        return Response("Hello")

    @staticmethod
    @view_authenticate
    def extract_detailed_reports(context, request, sessao):
        '''
        Responsavel por extrair relatorios mais detalhados, com:
            itens
            valores
            envolvidos
        '''
        return Response("Hello")

    @staticmethod
    @view_authenticate
    def extract_spreadsheets(context, request, sessao):
        return Response("Hello")

class ViewManager(ViewBase):

    @staticmethod
    @view_authenticate
    def add_users(context, request, sessao):
        # TODO: HTML responsepegar_moradores
        return Response("Hello")

    @staticmethod
    @view_authenticate
    def update_users(context, request, sessao):
        return Response("Hello")

    @staticmethod
    @view_authenticate
    def delete_users(context, request, sessao):
        return Response("Hello")
        
    @staticmethod
    @view_authenticate
    def get_users(context, request, sessao):
        return Response("Hello")