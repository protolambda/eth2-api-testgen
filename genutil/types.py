from typing import TypedDict, Dict, Any, NamedTuple, Callable, Iterator, Optional


class TestGen(NamedTuple):
    input: Dict[str, Any]
    code: int
    description: Optional[str]
    path: str
    post: Any


class TestGenGroup(NamedTuple):
    name: str
    # can generate the test cases by calling this
    gens_fn: Callable[[], Iterator[TestGen]]


class TestCase(TypedDict):
    input: Dict[str, Any]
    description: Optional[str]
    path: str
    code: int
    post: Optional[Any]
    response: Any
