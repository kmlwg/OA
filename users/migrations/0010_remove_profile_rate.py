# Generated by Django 2.2.7 on 2019-12-17 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20191217_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='rate',
        ),
    ]