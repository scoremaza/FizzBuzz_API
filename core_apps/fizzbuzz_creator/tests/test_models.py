import pytest

from core_apps.fizzbuzz_creator.models import FizzBuzz

def test_fizzbuzz_str(fizzbuzz):
    assert fizzbuzz.__str__() == f"This is {fizzbuzz.fizzbuzz_id} id message: {fizzbuzz.message}"