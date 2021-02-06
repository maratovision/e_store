# Generated by Django 3.1.5 on 2021-02-05 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0012_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default_image.png', upload_to='')),
                ('full_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('F', 'F'), ('M', 'M')], max_length=20)),
                ('description', models.TextField()),
                ('birth_date', models.DateField()),
                ('twitter_link', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
