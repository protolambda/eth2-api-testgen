from genutil import *


def gen_get_header():
    for mode in valid_block_ids:
        yield TestGen(input={'block_id': mode}, path=f'/eth/v1/beacon/headers/{mode}',
                      post=None, description=f'try block ID {mode}')
    for mode in invalid_block_ids:
        yield TestGen(input={'block_id': mode}, path=f'/eth/v1/beacon/headers/{mode}',
                      post=None, description=f'try block ID {mode}')
    for mode in nonexistent_block_ids:
        yield TestGen(input={'block_id': mode}, path=f'/eth/v1/beacon/headers/{mode}',
                      post=None, description=f'try block ID {mode}')

