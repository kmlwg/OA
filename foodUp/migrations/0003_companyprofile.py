# Generated by Django 2.2.6 on 2019-11-09 13:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodUp', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='company_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=40, unique=True)),
                ('phone_number', models.CharField(max_length=11)),
                ('time_opened', models.TimeField()),
                ('time_closed', models.TimeField()),
                ('rating', models.FloatField(default=0.0, validators=[django.core.validators.MaxValueValidator(10.0), django.core.validators.MinValueValidator(0.0)])),
                ('description', models.TextField()),
            ],
        ),
    ]
