# Generated by Django 4.2.6 on 2024-02-13 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aero_mx', '0002_alter_aircraft_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hangar',
            old_name='user',
            new_name='owner',
        ),
    ]
