import requests
from urllib import urlencode


class RESTConsumer(object):

    #region Constants
    HOST = "https://secure.splitwise.com/api/v3.0"
    #endregion
    
    #region Public Methods
    @classmethod
    def post_request(cls, uri, params, json_body, **kwargs):
        _uri = cls.HOST + uri
        _response = requests.post(
            _uri, 
            json_body, 
            params=urlencode(params), 
            **kwargs
        )

        if _response.status_code == 201:
            return _response
        else:
            raise ValueError()

    @classmethod
    def put_request(cls, uri, params, codigo, json_body, **kwargs):
        _uri = cls.HOST + uri + "/" + codigo
        _response = requests.put(
            _uri, 
            json_body, 
            params=urlencode(params), 
            **kwargs
        )

        if _response.status_code == 200:
            return _response
        else:
            raise ValueError()

    @classmethod
    def delete_request(cls, uri, params, codigo, **kwargs):
        _uri = cls.HOST + uri + "/" + codigo
        _response = requests.delete(_uri, params=urlencode(params), **kwargs)

        if _response.status_code == 200:
            return _response
        else:
            raise ValueError()

    @classmethod
    def get_all_request(cls, uri, params, **kwargs):
        _uri = cls.HOST + uri
        _response = requests.get(_uri, params=urlencode(params), **kwargs)

        if _response.status_code == 200:
            return _response
        else:
            raise ValueError()

    @classmethod
    def get_request(cls, uri, params, codigo, **kwargs):
        _uri = cls.HOST + uri + "/" + codigo
        _response = requests.get(_uri, params=urlencode(params), **kwargs)

        if _response.status_code == 200:
            return _response
        else:
            raise ValueError()
    #endregion

class OAuth2(object):
    pass
