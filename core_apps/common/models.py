import uuid

from django.db import models


class TimeStampedUUIDModel(models.Model):
    '''

    '''
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-creation_date", "-updated_date"]
