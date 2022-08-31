from core_apps.fizzbuzz_creator.models import FizzBuzz
import factory
import json
import pytest
from factories import FizzBuzzFactory



class TestFizzBuzzEndpoints:

    endpoint = 'api/v1/fizzbuzz/'
  

    @pytest.mark.django_db
    def test_list(self, api_client):

        response = api_client().get(
            self.endpoint
        )

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 10

   