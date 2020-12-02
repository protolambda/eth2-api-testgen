from typing import Iterator, Any
from genutil.types import TestGenGroup
from inspect import getmembers, isfunction


# a python generator yielding groups of API testcase generators...
def get_generators(src: Any) -> Iterator[TestGenGroup]:
    for (name, _) in getmembers(src, isfunction):
        if not name.startswith('gen_'):
            continue
        gfn = getattr(src, name)
        # strip off the `gen_`
        case_name = name
        if case_name.startswith('gen_'):
            case_name = case_name[4:]
        yield TestGenGroup(name=case_name, gens_fn=gfn)

