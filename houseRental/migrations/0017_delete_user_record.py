# Generated by Django 4.0.2 on 2022-07-09 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houseRental', '0016_remove_adminhouses_facility_remove_adminhouses_phone_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user_record',
        ),
    ]
