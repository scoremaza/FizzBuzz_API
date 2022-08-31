import django
from rest_framework.test import APIClient

django.setup()

import pytest
from pytest_factoryboy import register

from core_apps.fizzbuzz_creator.tests.factories import FizzBuzzFactory

register(FizzBuzzFactory)

@pytest.fixture
def fizzbuzz(db, fizz_buzz_factory):
    fizzbuzz_creation = fizz_buzz_factory.create()
    return fizzbuzz_creation

# conftest.py
@pytest.fixture
def api_client():
    return APIClient

