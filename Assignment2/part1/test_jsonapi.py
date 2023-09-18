import json
from src import *

## This is the test file for testing jsonapi

def test_encode_complex_number():
    number = complex(1, 2)
    actual = json.dumps(number, cls=jsonapi.BetterEncoder)
    assert actual == '{"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}'

def test_decode_complex_number():
    jsonfied_compelx_number = '{"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}'
    actual = json.loads(jsonfied_compelx_number, cls=jsonapi.BetterDecoder)
    assert actual == complex(1, 2)

def test_encode_range():
    rg = range(1, 9, 2)
    actual = json.dumps(rg, cls=jsonapi.BetterEncoder)
    assert actual == '{"start": 1, "stop": 9, "step": 2, "__extended_json_type__": "range"}'

def test_decode_range():
    jsonfied_range = '{"start": 1, "stop": 9, "step": 2, "__extended_json_type__": "range"}'
    actual = json.loads(jsonfied_range, cls=jsonapi.BetterDecoder)
    assert actual == range(1, 9, 2)

if __name__ == "__main__":
    test_encode_complex_number()
    test_decode_complex_number()
    test_encode_range()
    test_decode_range()
