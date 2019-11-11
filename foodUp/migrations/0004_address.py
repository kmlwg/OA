# Generated by Django 2.2.6 on 2019-11-09 13:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodUp', '0003_companyprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('building_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodUp.CompanyProfile')),
            ],
        ),
    ]
