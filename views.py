from pyramid.view import view_config
from pyramid.response import Response


class ViewBase(object):
    pass

class ViewAdministrador(ViewBase):

    @classmethod
    @view_config(
        route_name="relatorios", 
        request_method="GET", 
        permission="pegar_moradores"
    )
    def extrair_relatorio(cls, request):
        return Response("Hello %(name)s!" % request.matchdict)

    @classmethod
    @view_config(
        route_name="relatorios_detalhados", 
        request_method="GET", 
        permission="pegar_moradores"
    )
    def extrair_relatorios_detalhados(cls, request):
        '''
        Responsavel por extrair relatorios mais detalhados, com:
            itens
            valores
            envolvidos
        '''
        return Response("Hello %(name)s!" % request.matchdict)

    @classmethod
    @view_config(
        route_name="planilhas", 
        request_method="GET", 
        permission="pegar_moradores"
    )
    def extrair_planilhas(cls, request):
        return Response("Hello %(name)s!" % request.matchdict)

class ViewGerenciador(ViewBase):

    @classmethod
    @view_config(
        route_name="moradores", 
        request_method="POST", 
        permission="adicionar_morador"
    )
    def adicionar_moradores(cls, request):
        # TODO: HTML responsepegar_moradores
        return Response("Hello %(name)s!" % request.matchdict)

    @classmethod
    @view_config(
        route_name="morador", 
        request_method="PUT", 
        permission="atualizar_moradores"
    )
    def atualizar_moradores(cls, request):
        return Response("Hello %(name)s!" % request.matchdict)

    @classmethod
    @view_config(
        route_name="morador", 
        request_method="DELETE", 
        permission="excluir_moradores"
    )
    def excluir_moradores(cls, request):
        return Response("Hello %(name)s!" % request.matchdict)
        
    @classmethod
    @view_config(
        route_name="moradores", 
        request_method="GET", 
        permission="pegar_moradores"
    )
    def pegar_moradores(cls, request):
        return Response("Hello %(name)s!" % request.matchdict)