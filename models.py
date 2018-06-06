from json import dumps, loads
from batpay.utils import RESTConsumer


class ModelUser(RESTConsumer):
    
    #region Constructor
    def __init__(self, **kwargs):
        self._id = kwargs.get("id")
        self._first_name = kwargs.get("first_name")
        self._last_name = kwargs.get("last_name")
        self._email = kwargs.get("email")
        self._registration_status = kwargs.get("registration_status", None)
        self._locale = kwargs.get("locale", None)
        self._date_format = kwargs.get("date_format", "DD/MM/YYYY")
        self._default_currency = kwargs.get("default_currency", "BRL")
        self._default_group_id = kwargs.get("default_group_id", None)
        self._notifications = kwargs.get("notifications", {})
        self._picture = kwargs.get(
            "picture", 
            {
                "small":"", 
                "medium":"", 
                "large":""
            }
        )
    #endregion

    #region Propertys
    @property
    def id(self):
        return self._id
    @property
    def first_name(self):
        return self._first_name
    @property
    def last_name(self):
        return self._last_name
    @property
    def email(self):
        return self._email
    @property
    def registration_status(self):
        return self._registration_status
    @property
    def locale(self):
        return self._locale
    @property
    def date_format(self):
        return self._date_format
    @property
    def default_currency(self):
        return self._default_currency
    @property
    def default_group_id(self):
        return self._default_group_id
    @property
    def notifications(self):
        return self._notifications
    @property
    def picture(self):
        return self._picture

    @property
    def valid(self):
        try:
            self.validate()
            return True
        except Exception:
            return False
    #endregion

    #region Setters
    @id.setter
    def id(self, value):
        self._id = value
    @first_name.setter
    def first_name(self, value):
        self._first_name = value
    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    @email.setter
    def email(self, value):
        self._email = value
    @registration_status.setter
    def registration_status(self, value):
        self._registration_status = value
    @locale.setter
    def locale(self, value):
        self._locale = value
    @date_format.setter
    def date_format(self, value):
        self._date_format = value
    @default_currency.setter
    def default_currency(self, value):
        self._default_currency = value
    @default_group_id.setter
    def default_group_id(self, value):
        self._default_group_id = value
    @notifications.setter
    def notifications(self, value):
        self._notifications = value
    @picture.setter
    def picture(self, value):
        self._picture = value
    #endregion

    #region Public Methods
    @classmethod
    def get(cls, identity):
        _request = cls.get_request(
            "/get_current_user",
            identity
        )
        _user = loads(_request.body)
        _user = cls(**_user)
        return _user

    def validate(self):
        return True
    #endregion

class ModelFriend(RESTConsumer):

    #region Constructor
    def __init__(self, **kwargs):
        self._id = kwargs.get("id")
        self._first_name = kwargs.get("first_name")
        self._last_name = kwargs.get("last_name")
        self._email = kwargs.get("email")
        self._registration_status = kwargs.get("registration_status", None)
        self._balance = kwargs.get("balance", [])
        self._groups = kwargs.get("groups", [])
        self._updated_at = kwargs.get("updated_at", None)
        self._picture = kwargs.get(
            "picture", 
            {
                "small":"", 
                "medium":"", 
                "large":""
            }
        )
    #endregion

    #region Propertys
    @property
    def id(self):
        return self._id
    @property
    def first_name(self):
        return self._first_name
    def last_name(self):
        return self._last_name
    def email(self):
        return self._email
    def registration_status(self):
        return self._registration_status
    def balance(self):
        return self._balance
    def groups(self):
        return self._groups
    def updated_at(self):
        return self._updated_at
    def picture(self):
        return self._picture

    #region Setters
    @id.setter
    def id(self, value):
        self._id = value
    @first_name.setter
    def first_name(self, value):
        self._first_name = value
    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    @email.setter
    def email(self, value):
        self._email = value
    @registration_status.setter
    def registration_status(self, value):
        self._registration_status = value
    @balance.setter
    def balance(self, value):
        self._balance = value
    @groups.setter
    def groups(self, value):
        self._groups = value
    @updated_at.setter
    def updated_at(self, value):
        self._updated_at = value
    @picture.setter
    def picture(self, value):
        self._picture = value
    #endregion

    #region Public Methods
    def add(self):
        _json = dumps(self.__dict__)
        _request = self.post_request(
            "/get_current_user",
            _json
        )
        _user = loads(_request.body)
        _user = self(**_user)
        return _user
        
    def delete(self, identity):
        _request = self.delete_request(
            "/get_current_user",
            identity
        )
        return True

    @classmethod
    def get_all(cls):
        _request = cls.get_all_request()
            "/get_friends"
        )
        _friends = loads(_request.body)
        return _friends

    @classmethod
    def get(cls, identity):
        _request = cls.get_request(
            "/get_current_user",
            identity
        )
        _friend = loads(_request.body)
        _friend = cls(**_friend)
        return _friend
    #endregion

class ModelExpense(RESTConsumer):

    #region Constructor
    def __init__(self, **kwargs):
        self._id = kwargs.get("id")
        self._group_id = kwargs.get("group_id")
        self._friendship_id = kwargs.get("friendship_id")
        self._expense_bundle_id = kwargs.get("expense_bundle_id")
        self._payment = kwargs.get("payment")
        self._cost = kwargs.get("cost")
        self._date = kwargs.get("date")
        self._created_at = kwargs.get("created_at")
        self._created_by = kwargs.get("created_by")
        self._description = kwargs.get("description", None)
        self._details = kwargs.get("details", None)
        self._updated_at = kwargs.get("updated_at", None)
        self._updated_by = kwargs.get("updated_by", None)
        self._deleted_at = kwargs.get("deleted_at", None)
        self._deleted_by = kwargs.get("deleted_by", None)
        self._category = kwargs.get("category", None)
    #endregion

    #region Propertys
    @property
    def id(self):
        return self._id
    @property
    def group_id(self):
        return self._group_id
    @property
    def friendship_id(self):
        return self._friendship_id
    @property
    def expense_bundle_id(self):
        return self._expense_bundle_id
    @property
    def payment(self):
        return self._payment
    @property
    def cost(self):
        return self._cost
    @property
    def date(self):
        return self._date
    @property
    def created_at(self):
        return self._created_at
    @property
    def created_by(self):
        return self._created_by
    @property
    def description(self):
        return self._description
    @property
    def details(self):
        return self._details
    @property
    def updated_at(self):
        return self._updated_at
    @property
    def updated_by(self):
        return self._updated_by
    @property
    def deleted_at(self):
        return self._deleted_at
    @property
    def deleted_by(self):
        return self._deleted_by
    @property
    def category(self):
        return self._category
    #endregion

    #region Setters
    @id.setter
    def id(self, value):
        self._id = value
    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @friendship_id.setter
    def friendship_id(self, value):
        self._friendship_id = value
    @expense_bundle_id.setter
    def expense_bundle_id(self, value):
        self._expense_bundle_id = value
    @payment.setter
    def payment(self, value):
        self._payment = value
    @cost.setter
    def cost(self, value):
        self._cost = value
    @date.setter
    def date(self, value):
        self._date = value
    @created_at.setter
    def created_at(self, value):
        self._created_at = value
    @created_by.setter
    def created_by(self, value):
        self._created_by = value
    @description.setter
    def description(self, value):
        self._description = value
    @details.setter
    def details(self, value):
        self._details = value
    @updated_at.setter
    def updated_at(self, value):
        self._updated_at = value
    @updated_by.setter
    def updated_by(self, value):
        self._updated_by = value
    @deleted_at.setter
    def deleted_at(self, value):
        self._deleted_at = value
    @deleted_by.setter
    def deleted_by(self, value):
        self._deleted_by = value
    @category.setter
    def category(self, value):
        self._category = value
    #endregion

    #region Public Methods
    def add(self):
        _json = dumps(self.__dict__)
        _request = self.post_request(
            "/get_current_user",
            _json
        )
        _expense_attr = loads(_request.body)
        _expense = self(**_expense_attr)
        return _expense
        
    def delete(self):
        _request = self.delete_request(
            "/get_current_user",
            self.identity
        )
        return True

    @classmethod
    def get_all(cls):
        _expenses = []
        _request = cls.get_all_request()
            "/get_friends",
            
        )
        _expenses_attr = loads(_request.body)
        for _expense_attr in _expenses_attr:
            _expenses.append(cls(**_expenses_attr))
        return _expenses

    @classmethod
    def get(cls, identity):
        _request = cls.get_request(
            "/get_current_user",
            identity
        )
        _expense = loads(_request.body)
        _expense = cls(_expense**)
        return _expense
    #endregion

#TODO: talvez num futuro
class Parente(object):

    # TODO: Consumir SQL
    #region Construtor
    def __init__(self, **kwargs):
        self.nome = kwargs.get("nome")
        self.idade = kwargs.get("idade")
        self.celular = kwargs.get("celular")
        self.cep = kwargs.get("cep", None)
        self.logradouro = kwargs.get("logradouro", None)
        self.cidade = kwargs.get("cidade", None)
        self.estado = kwargs.get("estado", None)
        self.pais = kwargs.get("pais", None)
    #endregion

    #region Metodos Publicos
    def adicionar(self, **kwargs):
        pass

    def excluir(self):
        pass
    #endregion
