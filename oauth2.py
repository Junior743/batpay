import requests
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import MobileApplicationClient


class OAuth2(object):

    #region Globals
    session = None
    #endregion

    #region Constants
    # TODO: This configurations should are in __init__ file
    CLIENT_ID = '2IFtKvuwi5MMhHqwCr4rFocDPc4tfoR2pSzXqait'
    SCOPES = []
    AUTH_URL = 'https://secure.splitwise.com/oauth/authorize'
    #endregion
    
    @classmethod
    def authorize(cls):
        '''
        Method responsible for authorize the application
        '''
        import ipdb; ipdb.set_trace()
        _oauth = OAuth2Session(client=MobileApplicationClient(client_id=cls.CLIENT_ID), scope=cls.SCOPES)
        _authorization_url, _state = _oauth.authorization_url(cls.AUTH_URL)

        _session = requests.Session()
        _session = _session.get(_authorization_url)

        return _session
