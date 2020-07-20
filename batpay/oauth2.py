import requests
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient


class OAuth2(object):

    #region Globals
    session = None
    #endregion

    #region Constants
    # TODO: This configurations should are in .ini file
    CLIENT_ID = '2IFtKvuwi5MMhHqwCr4rFocDPc4tfoR2pSzXqait'
    CLIENT_SECRET = 'AAzHaABGKBBkGRPMg9jOFqoudLvNPq14GUNLXQMN'
    SCOPES = []
    AUTH_URI = 'https://secure.splitwise.com/oauth/authorize'
    TOKEN_URI = 'https://secure.splitwise.com/oauth/token'
    #endregion

    @classmethod
    def authorize(cls):
        '''
        Method responsible for authorize the application
        '''
        _client = BackendApplicationClient(client_id=cls.CLIENT_ID)
        _oauth = OAuth2Session(client=_client, scope=cls.SCOPES)
        _token = _oauth.fetch_token(token_url=cls.TOKEN_URI, client_id=cls.CLIENT_ID, client_secret=cls.CLIENT_SECRET)

        _session = _oauth

        return _session


#region Decorators
def view_authenticate(func):
    def func_wrapper(*param):
        import ipdb; ipdb.set_trace()
        _context = param[0]
        _request = param[1]
        _session = OAuth2.authorize()
        return func(_context, _request, _session)
    return func_wrapper
#endregion