# Generated by Django 3.1.5 on 2021-01-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210128_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='latitude',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='longtitude',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
    ]
