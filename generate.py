from typing import Tuple, Iterator
from genutil import *
import json
import os

import generators.beacon.blocks as beacon_blocks
import generators.beacon.headers as beacon_headers
import generators.beacon.genesis as beacon_genesis
import generators.beacon.pool as beacon_pool
import generators.beacon.states as beacon_states


def organize(v: str, grps: Iterator[TestGenGroup]) -> Iterator[Tuple[str, TestGenGroup]]:
    for g in grps:
        yield (v, g)


def all_generator_groups() -> Iterator[TestGenGroup]:
    yield from organize('beacon/blocks/', get_generators(beacon_blocks))
    yield from organize('beacon/headers/', get_generators(beacon_headers))
    yield from organize('beacon/genesis/', get_generators(beacon_genesis))
    yield from organize('beacon/pool/', get_generators(beacon_pool))
    yield from organize('beacon/states/', get_generators(beacon_states))
    # TODO many more


endpoint = "http://localhost:4001"

for (parent, case_group) in all_generator_groups():
    print(f"generating {parent}{case_group.name}")
    # TODO can filter tests at little added cost here: if case_group.name
    grp_path = "output/"+parent
    os.makedirs(grp_path, exist_ok=True)
    with open(grp_path + case_group.name + ".json", "wt") as f:
        cases = []
        for gen in case_group.gens_fn():
            print("running %-100s  # case %4d: %s" % (gen.path, len(cases), gen.description))
            case = run_gen(endpoint, gen)
            cases.append(case)
        json.dump(cases, f, indent=2)
