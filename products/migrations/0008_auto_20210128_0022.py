# Generated by Django 3.1.5 on 2021-01-27 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20210128_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
