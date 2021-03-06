from copy import deepcopy
from genutil import *


def gen_get_block_attestations():
    for id in valid_block_ids:
        yield TestGen(input={'block_id': id}, path=f'/eth/v1/beacon/blocks/{id}/attestations', code=200,
                      post=None, description=f'valid block atts req')
    for id in invalid_block_ids:
        yield TestGen(input={'block_id': id}, path=f'/eth/v1/beacon/blocks/{id}/attestations', code=405,
                      post=None, description=f'invalid block atts req')
    for id in nonexistent_block_ids:
        yield TestGen(input={'block_id': id}, path=f'/eth/v1/beacon/blocks/{id}/attestations', code=404,
                      post=None, description=f'non-existent block atts req')


def gen_get_block():
    for id in valid_block_ids:
        yield TestGen(input={'block_id': id}, path=f'/eth/v1/beacon/blocks/{id}', code=200,
                      post=None, description=f'valid block req')
    for id in invalid_block_ids:
        yield TestGen(input={'block_id': id}, path=f'/eth/v1/beacon/blocks/{id}', code=405,
                      post=None, description=f'invalid block req')
    for id in nonexistent_block_ids:
        yield TestGen(input={'block_id': id}, path=f'/eth/v1/beacon/blocks/{id}', code=404,
                      post=None, description=f'non-existent block req')


def gen_get_block_root():
    for id in valid_block_ids:
        yield TestGen(input={'block_id': id}, path=f'/eth/v1/beacon/blocks/{id}/root', code=200,
                      post=None, description=f'valid block req')
    for id in invalid_block_ids:
        yield TestGen(input={'block_id': id}, path=f'/eth/v1/beacon/blocks/{id}/root', code=405,
                      post=None, description=f'invalid block req')

    id = '1000000'
    yield TestGen(input={'block_id': id}, path=f'/eth/v1/beacon/blocks/{id}/root', code=404,
                  post=None, description=f'non-existent block req')
    # getting a block root with an unknown block root as input should just be 'ok'
    id = '0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    yield TestGen(input={'block_id': id}, path=f'/eth/v1/beacon/blocks/{id}/root', code=200,
                  post=None, description=f'non-existent block req')


# mainnet block, to get a status 200
valid_block = {
    "message": {
        "slot": "4341",
        "proposer_index": "21352",
        "parent_root": "0xc49d73c2b14186e1a7ac5a83894d6be86de85510f584e10bd1cc6af24281c58e",
        "state_root": "0xcc75ccd8f72395180e745f2c3429cb1c69e0eddedb8f1e15297ea9bcdbbb9172",
        "body": {
            "randao_reveal": "0xb6261601277aa61916c28d5587e8dcc7711702ed28093db18ff484f2a52dcc19a44ef74e9854561ebed77a0c432d3fa00bf284f99624b45094a83a3638594db34eb4cc2a1a8b7ebfda4bd75ac1a1b583d1d7c544aca6f6c60f5f24ee41c5a994",
            "eth1_data": {
                "deposit_root": "0xd1b9b16334c16b689426b0ff3ed6e1d6ea1143698274237ae912e4e6dd158a5a",
                "deposit_count": "27524",
                "block_hash": "0xaf5acf26938b4e04c40792e3d3afc885119da2f5753fd7f6686702a5a8eb519d"
            },
            "graffiti": "0xf09f90a057656c636f6d6520746f20746865204e657720426567696e6e696e67",
            "proposer_slashings": [],
            "attester_slashings": [],
            "attestations": [
                {
                    "aggregation_bits": "0xfffffffdffffdffffffffdffffffffff7f",
                    "data": {
                        "slot": "4340",
                        "index": "2",
                        "beacon_block_root": "0xc49d73c2b14186e1a7ac5a83894d6be86de85510f584e10bd1cc6af24281c58e",
                        "source": {
                            "epoch": "134",
                            "root": "0x2e47edf9e4ae70998223cdc9f89363c84608ecac4c856a7824da6c405df7a4a0"
                        },
                        "target": {
                            "epoch": "135",
                            "root": "0xd632a225b3d80abefcbc5ffa4991766adf13ce4fac455dd3fb8abba723f75ab4"
                        }
                    },
                    "signature": "0x91c6c061f78e617fdd42c5cbbf703a7176dec30699eb4cd4caa5f3cf7c0547eca6231dc070ba61ad15c8015a59204805197236c51abe4a5c7a2f8e250d2bfd99fbc4f54752f07b6a0021dbd45f3c5fb072a42280f02ebec8ecdeb99a3d99f46f"
                },
                {
                    "aggregation_bits": "0xffbfffffffffffffeffffffffffdffbf7f",
                    "data": {
                        "slot": "4340",
                        "index": "0",
                        "beacon_block_root": "0xc49d73c2b14186e1a7ac5a83894d6be86de85510f584e10bd1cc6af24281c58e",
                        "source": {
                            "epoch": "134",
                            "root": "0x2e47edf9e4ae70998223cdc9f89363c84608ecac4c856a7824da6c405df7a4a0"
                        },
                        "target": {
                            "epoch": "135",
                            "root": "0xd632a225b3d80abefcbc5ffa4991766adf13ce4fac455dd3fb8abba723f75ab4"
                        }
                    },
                    "signature": "0x8515c462f77b73966a34fea8eabb4bed98252182197eb066682cb4209c330090c6e5407b09508a4bd78629180228cbcf0cbe4f6bf2767c1c353682d32b584d00891ec5f359780061c2a84d053b131682aa953252d5bb0e706caa44e64d9a858d"
                },
                {
                    "aggregation_bits": "0xfffbfeffffffffdfffbfffffffffbfff7f",
                    "data": {
                        "slot": "4340",
                        "index": "4",
                        "beacon_block_root": "0xc49d73c2b14186e1a7ac5a83894d6be86de85510f584e10bd1cc6af24281c58e",
                        "source": {
                            "epoch": "134",
                            "root": "0x2e47edf9e4ae70998223cdc9f89363c84608ecac4c856a7824da6c405df7a4a0"
                        },
                        "target": {
                            "epoch": "135",
                            "root": "0xd632a225b3d80abefcbc5ffa4991766adf13ce4fac455dd3fb8abba723f75ab4"
                        }
                    },
                    "signature": "0xaf76f47ecf2b474640219c7aee013f175c5b89faf8c14329fa251bc16ea7008f3e29790415ea6dd4ebddd7a49b1448e70534ffa80ee42f99d3c9808f8689d2f19169faf975460ef29d9931d47f65854f272fd81a6f1b74035c3221caaaa8c7c1"
                },
                {
                    "aggregation_bits": "0xfffeffffdffffbfffffffff7fffffbff7e",
                    "data": {
                        "slot": "4340",
                        "index": "1",
                        "beacon_block_root": "0xc49d73c2b14186e1a7ac5a83894d6be86de85510f584e10bd1cc6af24281c58e",
                        "source": {
                            "epoch": "134",
                            "root": "0x2e47edf9e4ae70998223cdc9f89363c84608ecac4c856a7824da6c405df7a4a0"
                        },
                        "target": {
                            "epoch": "135",
                            "root": "0xd632a225b3d80abefcbc5ffa4991766adf13ce4fac455dd3fb8abba723f75ab4"
                        }
                    },
                    "signature": "0xb8ce93f301c896f8ba798626f03ea7d37492436a9c44f04845aa8763c14647580823e24349e23e5ea70a7628870318ff0c848b86cc031a9c38f3127e9769b477ffb8bfcc3712b4aa109109d866be0540ccf6d0d8278b5b46ccf9cd40bf30a765"
                },
                {
                    "aggregation_bits": "0xffffbfbefffffffffff7fbff7ffeffff7f",
                    "data": {
                        "slot": "4340",
                        "index": "3",
                        "beacon_block_root": "0xc49d73c2b14186e1a7ac5a83894d6be86de85510f584e10bd1cc6af24281c58e",
                        "source": {
                            "epoch": "134",
                            "root": "0x2e47edf9e4ae70998223cdc9f89363c84608ecac4c856a7824da6c405df7a4a0"
                        },
                        "target": {
                            "epoch": "135",
                            "root": "0xd632a225b3d80abefcbc5ffa4991766adf13ce4fac455dd3fb8abba723f75ab4"
                        }
                    },
                    "signature": "0xa1139b44b4cd028df27dff073e6fb2017a88558967c1d4a9bf5f427036e3349aac1ca30df6f6da1c9f8f81237a8fa04006d0a2ba65b3af4043c8c2d34bc41eeda30f1ff6fd6e9dd4df3a533769b927af8687e9c4faeb1feec5f39a2e9d590859"
                },
                {
                    "aggregation_bits": "0x0802290400008080010086049801007843",
                    "data": {
                        "slot": "4340",
                        "index": "1",
                        "beacon_block_root": "0xc49d73c2b14186e1a7ac5a83894d6be86de85510f584e10bd1cc6af24281c58e",
                        "source": {
                            "epoch": "134",
                            "root": "0x2e47edf9e4ae70998223cdc9f89363c84608ecac4c856a7824da6c405df7a4a0"
                        },
                        "target": {
                            "epoch": "135",
                            "root": "0xd632a225b3d80abefcbc5ffa4991766adf13ce4fac455dd3fb8abba723f75ab4"
                        }
                    },
                    "signature": "0xab6dcf59db249283f759c785d994e86c81d39bc36b3ae5b1b8a91af946fc5247e45a812f3e1fd166a0a4f0567c9984910a656d740473fcde306c2d2f43882535d66f460070d3aae0fab93af69f08eeee9a5c82cd9d7d5b3f280eca41e5409520"
                }
            ],
            "deposits": [],
            "voluntary_exits": []
        }
    },
    "signature": "0xadd429396084d13ac43f8c9051439f9dd6fe33b6f62ed0883214d300dd61302b35a4eca59fc097bbc836537e5958069913e30bc287c02121c8804621ed4c41a583b04cf9122881cbecd1bfcb4ce5c3d74e5d86aa57e9a3a8a3e3146c3d9dbf25"
}

invalid_block = deepcopy(valid_block)
# modify something silly to make it invalid. It will be published, but with 202 code.
invalid_block['message']['slot'] = '123'


def gen_post_block():
    yield TestGen(input={'block': valid_block}, path=f'/eth/v1/beacon/blocks/', code=200,
                  post=valid_block, description=f'valid block publish')
    yield TestGen(input={'block': invalid_block}, path=f'/eth/v1/beacon/blocks/', code=202,
                  post=invalid_block, description=f'invalid block publish')

