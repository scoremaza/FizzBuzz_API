# Generated by Django 3.2.11 on 2022-08-31 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fizzbuzz_creator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fizzbuzz',
            name='message',
            field=models.TextField(help_text='Message from the sender'),
        ),
        migrations.AlterField(
            model_name='fizzbuzz',
            name='useragent',
            field=models.TextField(help_text='Client User-Agent HTTP header'),
        ),
    ]