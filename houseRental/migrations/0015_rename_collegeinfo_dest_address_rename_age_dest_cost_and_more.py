# Generated by Django 4.0.2 on 2022-07-08 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houseRental', '0014_alter_dest_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dest',
            old_name='collegeinfo',
            new_name='ADDRESS',
        ),
        migrations.RenameField(
            model_name='dest',
            old_name='age',
            new_name='COST',
        ),
        migrations.RenameField(
            model_name='dest',
            old_name='url',
            new_name='ENTER_LOCATION',
        ),
        migrations.RenameField(
            model_name='dest',
            old_name='name',
            new_name='OWNER_NAME',
        ),
        migrations.RenameField(
            model_name='dest',
            old_name='img',
            new_name='UPLOAD_HOUSE_IMAGE',
        ),
    ]
