# Generated by Django 4.0 on 2022-03-09 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_restaurant_mamanger'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='mamanger',
            new_name='manager',
        ),
    ]
