# Generated by Django 5.0.6 on 2024-06-06 21:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=36, unique=True)),
                ('country', models.CharField(max_length=36, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='ing/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('price_per_night', models.PositiveSmallIntegerField(default=0)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='ImageRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='ing/')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.room')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('age', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('photo', models.ImageField(upload_to='')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField()),
                ('value', models.CharField(choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], max_length=16)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.comment', verbose_name='Родитель')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.hotel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mysite.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateTimeField()),
                ('check_out_date', models.DateTimeField()),
                ('total_price', models.PositiveSmallIntegerField()),
                ('status', models.CharField(choices=[('Бронированный', 'Бронированный'), ('Занят', 'Занят'), ('Свободный', 'Свободный')], max_length=16)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.room')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mysite.userprofile')),
            ],
        ),
    ]
