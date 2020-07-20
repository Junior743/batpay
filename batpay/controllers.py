from batpay.oauth2 import OAuth2
from batpay.utils import RESTConsumer
from batpay.oauth2 import authenticate


class ControllerAuthorization(object):

    #region Built-in
    def __call__(self):
        OAuth2.authorize()
    #endregion

class ControllerExcel(object):

    #region Metodos Publicos
    @staticmethod
    def distribuir_contas(session):
        pass
    #endregion

class ControllerPDF(object):

    #region Metodos Publicos
    @staticmethod
    def distribuir_contas(session):
        pass
    #endregion