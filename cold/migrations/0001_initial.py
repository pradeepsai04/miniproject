# Generated by Django 4.0.2 on 2022-09-14 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminhouses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IMAGE', models.ImageField(default='NULL', upload_to='pics')),
                ('PRICE', models.IntegerField(default=250)),
                ('PLACE', models.TextField(default='VIZAG')),
            ],
        ),
        migrations.CreateModel(
            name='adminhouses2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IMAGE', models.ImageField(default='NULL', upload_to='pics')),
                ('PRICE', models.IntegerField(default=250)),
                ('PLACE', models.TextField(default='VIZAG')),
            ],
        ),
        migrations.CreateModel(
            name='adminhouses3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IMAGE', models.ImageField(default='NULL', upload_to='pics')),
                ('PRICE', models.IntegerField(default=250)),
                ('PLACE', models.TextField(default='VIZAG')),
            ],
        ),
        migrations.CreateModel(
            name='dest1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('cost', models.IntegerField(default=15)),
                ('img', models.ImageField(upload_to='pics quaality')),
                ('facility', models.TextField(default='3BHK')),
                ('phone', models.IntegerField(default=15)),
            ],
        ),
        migrations.CreateModel(
            name='house',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('cost', models.IntegerField(default=15)),
                ('img', models.ImageField(upload_to='pics quaality')),
                ('facility', models.TextField(default='3BHK')),
                ('phone', models.IntegerField(default=15)),
            ],
        ),
        migrations.CreateModel(
            name='MILL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OWNER_NAME', models.CharField(max_length=100)),
                ('COST', models.IntegerField(default=100)),
                ('UPLOAD_IMAGE1', models.ImageField(default='NULL', upload_to='new pics')),
                ('UPLOAD_IMAGE2', models.ImageField(default='NULL', upload_to='new pics')),
                ('UPLOAD_IMAGE3', models.ImageField(default='NULL', upload_to='new pics')),
                ('ADDRESS', models.TextField(default='vignan')),
                ('ADDRESS_URL', models.URLField(default='NULL')),
                ('ENTER_LOCATION', models.URLField(default='NULL', max_length=2000)),
                ('STATE', models.CharField(choices=[('vizag', 'vizag'), ('krishna', 'krishna'), ('nellore', 'nellore'), ('east godavari', 'east godavari'), ('chittor', 'chittor'), ('guntur', 'guntur'), ('srikakulam', 'srikakulam'), ('kakinada', 'kakinada')], default='krishna', max_length=50)),
            ],
        ),
    ]