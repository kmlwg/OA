# Generated by Django 2.2.6 on 2019-12-17 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodUp', '0004_auto_20191217_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='com',
            new_name='comment',
        ),
    ]
