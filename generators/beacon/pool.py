from genutil import *


def gen_get_pool_attestations():
    yield TestGen(input={}, path=f'/eth/v1/beacon/pool/attestations', code=200,
                  post=None, description=f'get all attestations')

    yield TestGen(input={'slot': 100, 'committee_index': 1}, path=f'/eth/v1/beacon/pool/attestations?committee_index=1&slot=100', code=200,
                  post=None, description=f'get attestations by slot and committee_index')

    yield TestGen(input={'slot': 100}, path=f'/eth/v1/beacon/pool/attestations?slot=100', code=200,
                  post=None, description=f'get attestations by slot')

    yield TestGen(input={'committee_index': 1}, path=f'/eth/v1/beacon/pool/attestations?committee_index=1', code=200,
                  post=None, description=f'get attestations by committee_index')

    # invalid pool queries will just result in empty responses, no error codes.
    yield TestGen(input={'slot': 10000000}, path=f'/eth/v1/beacon/pool/attestations?slot=10000000', code=200,
                  post=None, description=f'get attestations high but valid slot')

    yield TestGen(input={'committee_index': 30}, path=f'/eth/v1/beacon/pool/attestations?committee_index=30', code=200,
                  post=None, description=f'get attestations high committee_index')

    yield TestGen(input={'committee_index': 30, 'slot': 100}, path=f'/eth/v1/beacon/pool/attestations?committee_index=30&slot=100', code=200,
                  post=None, description=f'get attestations slot with combined query and high committee_index')

# TODO: test submit attestations


def gen_get_pool_attester_slashings():
    yield TestGen(input={}, path=f'/eth/v1/beacon/pool/attester_slashings', code=200,
                  post=None, description=f'get all attester slashings')

# TODO: test submit attester slashing


def gen_get_pool_proposer_slashings():
    yield TestGen(input={}, path=f'/eth/v1/beacon/pool/proposer_slashings', code=200,
                  post=None, description=f'get all proposer slashings')


# TODO: test submit voluntary exit

def gen_get_pool_voluntary_exits():
    yield TestGen(input={}, path=f'/eth/v1/beacon/pool/voluntary_exits', code=200,
                  post=None, description=f'get all voluntary exits')

