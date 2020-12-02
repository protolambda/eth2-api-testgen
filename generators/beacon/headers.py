from genutil import *


def gen_get_header():
    for id in valid_block_ids:
        yield TestGen(input={'block_id': id}, path=f'/eth/v1/beacon/headers/{id}', code=200,
                      post=None, description=f'valid block header req')
    for id in invalid_block_ids:
        yield TestGen(input={'block_id': id}, path=f'/eth/v1/beacon/headers/{id}', code=405,
                      post=None, description=f'invalid block header req')
    for id in nonexistent_block_ids:
        yield TestGen(input={'block_id': id}, path=f'/eth/v1/beacon/headers/{id}', code=404,
                      post=None, description=f'non-existent block header req')


def gen_get_block_headers():
    yield TestGen(input={}, path=f'/eth/v1/beacon/headers', code=200,
                  post=None, description=f'headers search, head slots by default')

    yield TestGen(input={'slot': 100}, path=f'/eth/v1/beacon/headers?slot=100', code=200,
                  post=None, description=f'headers search, slot-only filter')

    yield TestGen(input={'slot': 100,
                         'parent_root': '0x629ae1587895043076500f4f5dcb202a47c2fc95d5b5c548cb83bc97bd2dbfe1'},
                  path=f'/eth/v1/beacon/headers?slot=100&parent_root=0x629ae1587895043076500f4f5dcb202a47c2fc95d5b5c548cb83bc97bd2dbfe1',
                  code=200,
                  post=None, description=f'headers search, slot and parent root filter')

    yield TestGen(input={'slot': 100,
                         'parent_root': '0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'},
                  path=f'/eth/v1/beacon/headers?slot=100&parent_root=0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                  code=404,
                  post=None, description=f'headers search, slot but unknown parent root filter')

    yield TestGen(input={'parent_root': '0x629ae1587895043076500f4f5dcb202a47c2fc95d5b5c548cb83bc97bd2dbfe1'},
                  path=f'/eth/v1/beacon/headers?parent_root=0x629ae1587895043076500f4f5dcb202a47c2fc95d5b5c548cb83bc97bd2dbfe1',
                  code=200,
                  post=None, description=f'headers search, parent root filter')

    yield TestGen(input={'parent_root': '0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'},
                  path=f'/eth/v1/beacon/headers?parent_root=0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                  code=404,
                  post=None, description=f'headers search, unknown parent root filter')
