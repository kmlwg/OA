# Generated by Django 2.2.6 on 2019-11-16 13:09

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('pizza', 'pizza'), ('beer', 'beer'), ('pasta', 'pasta'), ('None', 'None')], default=None, max_length=21),
        ),
    ]
