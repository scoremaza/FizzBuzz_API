from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class FizzbuzzCreatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.fizzbuzz_creator'
    verbose_name = _('FizzBuzz_Creator')