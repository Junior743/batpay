from oauth2 import OAuth2
from utils import RESTConsumer
from oauth2 import authenticate


class ControllerAuthorization(object):

    #region Built-in
    def __call__(self):
        OAuth2.authorize()
    #endregion

class ControllerExcel(object):

    #region Metodos Publicos
    @staticmethod
    def distribuir_contas(sessao):
        pass
    #endregion

class ControllerPDF(object):

    #region Metodos Publicos
    @staticmethod
    def distribuir_contas(sessao):
        pass
    #endregion