# Generated by Django 4.0.2 on 2022-06-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houseRental', '0002_dest_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='dest',
            name='college',
            field=models.CharField(default='vignan', max_length=100),
        ),
    ]