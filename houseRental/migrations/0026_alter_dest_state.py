# Generated by Django 4.0.2 on 2022-08-15 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houseRental', '0025_alter_adminhouses_place_alter_adminhouses2_place_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dest',
            name='STATE',
            field=models.CharField(choices=[('Mr', 'Mr.'), ('Mrs', 'Mrs'), ('Other(Specify)', 'Other(Specify)')], default='krishna', max_length=50),
        ),
    ]