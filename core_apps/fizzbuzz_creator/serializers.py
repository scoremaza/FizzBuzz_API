from dataclasses import fields
from rest_framework import serializers

from .models import FizzBuzz


class FizzBuzzSerializers(serializers.ModelSerializer):
    """ """

    class Meta:
        model = FizzBuzz
        fields = '__all__'
        read_only_fields = ('useragent',)

    def create(self, validated_data):
        """Create and return a new user"""
        fizz_buzz = FizzBuzz.objects.create(
            message=validated_data['message'],
            useragent = validated_data['useragent']
        )

        return fizz_buzz