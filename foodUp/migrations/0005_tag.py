# Generated by Django 2.2.6 on 2019-11-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodUp', '0004_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('companies', models.ManyToManyField(to='foodUp.CompanyProfile')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]