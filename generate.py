from typing import Tuple, Iterator
from genutil import *
import json
import os

import generators.beacon.blocks as beacon_blocks

def organize(v: str, grps: Iterator[TestGenGroup]) -> Iterator[Tuple[str, TestGenGroup]]:
    for g in grps:
        yield (v, g)


def all_generator_groups() -> Iterator[TestGenGroup]:
    yield from organize('beacon/blocks/', get_generators(beacon_blocks))
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
            print(f"running {gen.path}")
            case = run_gen(endpoint, gen)
            cases.append(case)
        json.dump(cases, f, indent=2)
