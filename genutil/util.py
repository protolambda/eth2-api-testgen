valid_block_ids = [
    # valid
    'genesis', 'head', 'finalized', '100', '0xb6c2a16aa85959604baba5344e869cabe1d096bb179d57e61fdca933f5ec7bf5'
]

invalid_block_ids = [
    # invalid
    'wut',
]

nonexistent_block_ids = [
    '1000000000',
    '0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
]

valid_state_ids = [
    # valid
    'genesis', 'head', 'justified', 'finalized', '100',
    '0xcc75ccd8f72395180e745f2c3429cb1c69e0eddedb8f1e15297ea9bcdbbb9172'
]

invalid_state_ids = [
    # invalid
    'wut',
]

nonexistent_state_ids = [
    '1000000000',
    '0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
]

valid_validator_ids = [
    # valid
    '0', '22000'
]

invalid_validator_ids = [
    # invalid
    'morty',
]

nonexistent_validator_ids = [
    '99999999',
    '0xa25da1827014cd3bc6e7b70f1375750935a16f00fbe186cc477c204d330cac7ee060b68587c5cdcfae937176a4dd2962'
]

validator_statuses_full = [
    'pending_initialized',
    'pending_queued',
    'active_ongoing',
    'active_exiting',
    'active_slashed',
    'exited_unslashed',
    'exited_slashed',
    'withdrawal_possible',
    'withdrawal_done',
    'active',
    'pending',
    'exited',
    'withdrawal',
]

validator_statuses = [
    'pending',
    'active',
    'exited',
    'withdrawn',
]
