# Generated by Django 4.0.2 on 2022-09-14 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cold', '0002_mill_choose_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mill',
            name='ADDRESS_URL',
        ),
    ]