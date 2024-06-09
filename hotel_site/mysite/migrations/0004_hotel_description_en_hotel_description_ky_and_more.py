# Generated by Django 5.0.6 on 2024-06-08 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_alter_room_price_per_night'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='name_en',
            field=models.CharField(max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='name_ky',
            field=models.CharField(max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='name_ru',
            field=models.CharField(max_length=36, null=True),
        ),
    ]