from genutil import *


def gen_get_header():
    for mode in valid_block_ids:
        yield TestGen(input={'block_id': mode}, path=f'/eth/v1/beacon/headers/{mode}', code=200,
                      post=None, description=f'valid block header req')
    for mode in invalid_block_ids:
        yield TestGen(input={'block_id': mode}, path=f'/eth/v1/beacon/headers/{mode}', code=405,
                      post=None, description=f'invalid block header req')
    for mode in nonexistent_block_ids:
        yield TestGen(input={'block_id': mode}, path=f'/eth/v1/beacon/headers/{mode}', code=404,
                      post=None, description=f'non-existent block header req')

