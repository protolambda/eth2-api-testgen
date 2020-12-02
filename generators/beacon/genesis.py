from genutil import *


def gen_get_genesis():
    yield TestGen(input={}, path=f'/eth/v1/beacon/genesis', code=200,
                  post=None, description=f'request genesis info')
