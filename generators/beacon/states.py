
from genutil import *


def gen_get_committees():
    yield TestGen(input={'state_id': '123', 'slot': 123}, path=f'/eth/v1/beacon/states/123/committees?slot=123', code=200,
                  post=None, description=f'request committees of state with slot query')

    # in epoch 135
    id_root_epoch_135 = '0xcc75ccd8f72395180e745f2c3429cb1c69e0eddedb8f1e15297ea9bcdbbb9172'
    yield TestGen(input={'state_id': id_root_epoch_135, 'slot': 130*32}, path=f'/eth/v1/beacon/states/{id_root_epoch_135}/committees?slot={130*32}', code=400,
                  post=None, description=f'request committees of state with inconsistent slot-block query')

    yield TestGen(input={'state_id': id_root_epoch_135, 'slot': 135*32}, path=f'/eth/v1/beacon/states/{id_root_epoch_135}/committees?slot={135*32}', code=200,
                  post=None, description=f'request committees of state with consistent slot-block query')

    for id in valid_state_ids:
        yield TestGen(input={'state_id': id}, path=f'/eth/v1/beacon/states/{id}/committees', code=200,
                      post=None, description=f'request committees of state')

    id = 120
    yield TestGen(input={'state_id': id, 'index': 1}, path=f'/eth/v1/beacon/states/{id}/committees?index=1', code=200,
                  post=None, description=f'request committees of state with committee index query')

    yield TestGen(input={'state_id': id, 'epoch': 100//32}, path=f'/eth/v1/beacon/states/{id}/committees?epoch={100//32}', code=200,
                  post=None, description=f'request committees of state with epoch query')

    yield TestGen(input={'state_id': id, 'slot': 123, 'index': 1}, path=f'/eth/v1/beacon/states/{id}/committees?slot=123&index=1', code=200,
                  post=None, description=f'request committees of state with combined query, and future slot')

    for id in invalid_state_ids:
        yield TestGen(input={'state_id': id}, path=f'/eth/v1/beacon/states/{id}/committees', code=400,
                      post=None, description=f'request committees of invalid state')

    for id in nonexistent_state_ids:
        yield TestGen(input={'state_id': id}, path=f'/eth/v1/beacon/states/{id}/committees', code=404,
                      post=None, description=f'request committees of unknown state')


def _state_getter(name: str):
    for id in valid_state_ids:
        yield TestGen(input={'state_id': id}, path=f'/eth/v1/beacon/states/{id}/{name}', code=200,
                      post=None, description=f'request {name} of state')
    for id in invalid_state_ids:
        yield TestGen(input={'state_id': id}, path=f'/eth/v1/beacon/states/{id}/{name}', code=400,
                      post=None, description=f'request {name} of invalid state')
    for id in nonexistent_state_ids:
        yield TestGen(input={'state_id': id}, path=f'/eth/v1/beacon/states/{id}/{name}', code=404,
                      post=None, description=f'request {name} of unknown state')


def gen_get_finality_checkpoints():
    yield from _state_getter('finality_checkpoints')


def gen_get_fork():
    yield from _state_getter('fork')


def gen_get_state_root():
    yield from _state_getter('root')


def gen_get_validator():
    for val_id in invalid_validator_ids:
        for id in valid_state_ids:
            yield TestGen(input={'state_id': id}, path=f'/eth/v1/beacon/states/{id}/validators/{val_id}', code=400,
                          post=None, description=f'request invalid validator {val_id} of state')

    for val_id in nonexistent_validator_ids:
        for id in valid_state_ids:
            # missing validator ids don't cause 404
            yield TestGen(input={'state_id': id}, path=f'/eth/v1/beacon/states/{id}/validators/{val_id}', code=400,
                          post=None, description=f'request non-existent validator {val_id} of state')

    for val_id in valid_validator_ids:
        for id in valid_state_ids:
            yield TestGen(input={'state_id': id}, path=f'/eth/v1/beacon/states/{id}/validators/{val_id}', code=200,
                          post=None, description=f'request validator {val_id} of state')
        for id in invalid_state_ids:
            yield TestGen(input={'state_id': id}, path=f'/eth/v1/beacon/states/{id}/validators/{val_id}', code=400,
                          post=None, description=f'request validator {val_id} of invalid state')
        for id in nonexistent_state_ids:
            yield TestGen(input={'state_id': id}, path=f'/eth/v1/beacon/states/{id}/validators/{val_id}', code=404,
                          post=None, description=f'request validator {val_id} of unknown state')


def gen_get_validator_balances():
    for id in valid_state_ids:
        yield TestGen(input={'state_id': id}, path=f'/eth/v1/beacon/states/{id}/validator_balances', code=200,
                      post=None, description=f'request all balances of state')
    for id in invalid_state_ids:
        yield TestGen(input={'state_id': id}, path=f'/eth/v1/beacon/states/{id}/validator_balances', code=400,
                      post=None, description=f'request all balances of invalid state')
    for id in nonexistent_state_ids:
        yield TestGen(input={'state_id': id}, path=f'/eth/v1/beacon/states/{id}/validator_balances', code=404,
                      post=None, description=f'request all balances of unknown state')

    id = 100
    yield TestGen(input={'state_id': id, 'val_ids': []}, path=f'/eth/v1/beacon/states/{id}/validator_balances?id=', code=200,
                  post=None, description=f'request no balances of valid state')

    val_ids = [100, 102, 300]
    yield TestGen(input={'state_id': id, 'val_ids': val_ids},
                  path=f'/eth/v1/beacon/states/{id}/validator_balances?id={",".join(map(str, val_ids))}', code=200,
                  post=None, description=f'request valid validator balances of valid state')

    val_ids = valid_validator_ids  # different types of validator ids in the same array!
    yield TestGen(input={'state_id': id, 'val_ids': val_ids},
                  path=f'/eth/v1/beacon/states/{id}/validator_balances?id={",".join(map(str, val_ids))}', code=200,
                  post=None, description=f'request valid but mixed-type validator balances of valid state')

    val_ids = [100, 102, 300, 9999999]
    yield TestGen(input={'state_id': id, 'val_ids': val_ids},
                  path=f'/eth/v1/beacon/states/{id}/validator_balances?id={",".join(map(str, val_ids))}', code=200,
                  post=None, description=f'request partially valid validator balances of valid state')


def gen_get_validators():
    # don't do queries for all validators on valid state. Try limited lookups instead. Results are too large.

    for id in invalid_state_ids:
        yield TestGen(input={'state_id': id}, path=f'/eth/v1/beacon/states/{id}/validators', code=400,
                      post=None, description=f'request all validators of invalid state')
    for id in nonexistent_state_ids:
        yield TestGen(input={'state_id': id}, path=f'/eth/v1/beacon/states/{id}/validators', code=404,
                      post=None, description=f'request all validators of unknown state')

    id = 3000  # some time where we have different validator statuses in the state
    for validator_status in validator_statuses:
        yield TestGen(input={'state_id': id, 'validator_statuses': [validator_status]},
                      path=f'/eth/v1/beacon/states/{id}/validators?status={validator_status}', code=200,
                      post=None, description=f'request all validators of state, filtered by single status')

    statuses = ['waiting_for_eligibility', 'withdrawn']
    yield TestGen(input={'state_id': id, 'validator_statuses': statuses},
                  path=f'/eth/v1/beacon/states/{id}/validators?status={",".join(statuses)}', code=200,
                  post=None, description=f'request all validators of state, filtered by multiple validator statuses')

    id = 100
    yield TestGen(input={'state_id': id, 'val_ids': []}, path=f'/eth/v1/beacon/states/{id}/validators?id=', code=200,
                  post=None, description=f'request no validators of valid state')

    val_ids = [100, 102, 300]
    for id in valid_state_ids:
        yield TestGen(input={'state_id': id, 'val_ids': val_ids},
                      path=f'/eth/v1/beacon/states/{id}/validator_balances?id={",".join(map(str, val_ids))}', code=200,
                      post=None, description=f'request valid validators of valid state')

    id = 100
    val_ids = valid_validator_ids  # different types of validator ids in the same array!
    yield TestGen(input={'state_id': id, 'val_ids': val_ids},
                  path=f'/eth/v1/beacon/states/{id}/validators?id={",".join(map(str, val_ids))}', code=200,
                  post=None, description=f'request valid but mixed-type id validators of valid state')

    val_ids = [100, 102, 300, 9999999]  # invalid parts are ignored in response
    yield TestGen(input={'state_id': id, 'val_ids': val_ids},
                  path=f'/eth/v1/beacon/states/{id}/validators?id={",".join(map(str, val_ids))}', code=200,
                  post=None, description=f'request partially valid validator ids of valid state')
