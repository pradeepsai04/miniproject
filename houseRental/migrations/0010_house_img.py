# Generated by Django 4.0.2 on 2022-07-06 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houseRental', '0009_user_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='img',
            field=models.ImageField(default='NULL', upload_to='pics'),
        ),
    ]
