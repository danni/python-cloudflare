from .. import util
from . import dns_records

ENDPOINT = 'zones'

def get(auth, params=None):
    if type(params) is dict:
        return util.call(auth, 'GET', ENDPOINT, params)
    elif type(params) is str:
        return util.call(auth, 'GET', ENDPOINT + '/' + params)