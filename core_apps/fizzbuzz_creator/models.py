from importlib.metadata import requires
from django.db import models
from django.utils.translation import gettext_lazy as _
from core_apps.common.models import TimeStampedUUIDModel


class FizzBuzz(TimeStampedUUIDModel):
    '''
    TODO:
    '''
    fizzbuzz_id = models.BigAutoField(primary_key=True, editable=False)
    useragent = models.TextField( help_text="Client User-Agent HTTP header", blank=False, null=False)
    message = models.TextField(help_text="Message from the sender",blank=False, null=False)


    def __str__(self):
        return f'This is {self.fizzbuzz_id} id message: {self.message}'
    


    







