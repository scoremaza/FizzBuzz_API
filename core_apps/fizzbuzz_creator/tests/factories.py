import uuid
import factory
from faker import Factory as FakerFactory
from faker.providers import DynamicProvider
from random import randint
from pytest_factoryboy import register
from core_apps.fizzbuzz_creator.models import FizzBuzz


faker = FakerFactory.create()

faker.seed(0)


useragent_provider = DynamicProvider(
     provider_name="useragent",
     elements = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ],
)

faker.add_provider(useragent_provider)


@register
class FizzBuzzFactory(factory.django.DjangoModelFactory):
    '''
    TODO:
    '''
    
    id = factory.LazyAttribute(lambda x: uuid.uuid4())
    fizzbuzz_id  = factory.LazyAttribute(lambda x: randint(1,20))
    creation_date = factory.LazyAttribute(lambda x: faker.date_time())
    updated_date = factory.LazyAttribute(lambda x: faker.date_time())
    message = factory.LazyAttribute(lambda x: faker.sentence(nb_words=10))
    useragent = factory.LazyAttribute(lambda x: faker.useragent)


    

    class Meta:
        model = FizzBuzz