from batpay.oath import OAuth
from batpay.utils import ConsumidorREST


class ControllerAuthorization(object):

    #region Built-in
    def __call__(self):
        OAuth.authorize()
    #endregion

class ControllerExcel(object):

    #region Metodos Publicos
    def distribuir_contas(self):
        pass
    #endregion

class ControllerPDF(object):

    #region Metodos Publicos
    def distribuir_contas(self):
        pass
    #endregion