from django.contrib import admin

from . import models

class FizzBuzzAdmin(admin.ModelAdmin):
    list_display = ["fizzbuzz_id", "message", "creation_date", "useragent", "id"]
    list_display_links = [ "id"]


admin.site.register(models.FizzBuzz, FizzBuzzAdmin)