import json
import functools
import os

_ASSETS = os.path.join(os.path.dirname(__file__), "assets")


@functools.cache
def numbers():
    with open(os.path.join(_ASSETS, "numbers.json"), encoding="utf-8") as f:
        return json.load(f)
