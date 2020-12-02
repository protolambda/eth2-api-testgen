from typing import Tuple
from genutil import *
import json
import os

import generators.beacon.blocks as beacon_blocks

def organize(v: str, grps: Generator[TestGenGroup]) -> Generator[Tuple[str, TestGenGroup]]:
    for g in grps:
        yield (v, g)


def all_generator_groups()-> Generator[TestGenGroup]:
    yield from organize('beacon/blocks/', get_generators(beacon_blocks))
    # TODO many more


endpoint = "http://localhost:4000/"

for (parent, case_group) in all_generator_groups():
    print(f"generating {parent}/{case_group.name}")
    # TODO can filter tests at little added cost here: if case_group.name
    grp_path = "output/"+parent
    os.makedirs(grp_path, exist_ok=True)
    with open(grp_path + "/" + case_group.name + ".json", "wt") as f:
        cases = []
        for gen in case_group.gens_fn():
            print(f"running {gen.__name__}")
            case = run_gen(endpoint, gen)
            cases.append(case)
        json.dump(cases, f)
