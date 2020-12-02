from genutil.types import TestGen, TestCase
import requests


def run_gen(endpoint: str, generator: TestGen) -> TestCase:
    if generator.post is None:
        r = requests.get(generator.path)
    else:
        r = requests.post(endpoint + generator.path, data=generator.post)
    return TestCase(input=generator.input, path=generator.path, description=generator.description,
                    code=int(r.status_code), post=generator.post, response=r.json())

