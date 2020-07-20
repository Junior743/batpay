from pyramid.view import view_config
from pyramid.response import Response

from batpay.oauth2 import view_authenticate


class ViewBase(object):
    pass

class ViewAdministrator(ViewBase):

    @staticmethod
    @view_authenticate
    def extract_expenses_reports(context, request, session):
        '''
        Responsavel por extrair relatorios mais detalhados, com:
            itens
            valores
            envolvidos
        '''
        import ipdb; ipdb.set_trace()
        _result = session.get("https://secure.splitwise.com/api/v3.0/get_groups")
        return Response("Hello")

class ViewManager(ViewBase):

    @staticmethod
    @view_authenticate
    def add_users(context, request, session):
        # TODO: HTML responsepegar_moradores
        return Response("Hello")

    @staticmethod
    @view_authenticate
    def update_users(context, request, session):
        return Response("Hello")

    @staticmethod
    @view_authenticate
    def delete_users(context, request, session):
        return Response("Hello")
        
    @staticmethod
    @view_authenticate
    def get_users(context, request, session):
        return Response("Hello")