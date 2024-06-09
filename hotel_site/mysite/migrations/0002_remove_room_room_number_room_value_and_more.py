# Generated by Django 5.0.6 on 2024-06-06 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_number',
        ),
        migrations.AddField(
            model_name='room',
            name='value',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], default=1, max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='value',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=16),
        ),
        migrations.AlterField(
            model_name='room',
            name='capacity',
            field=models.CharField(choices=[('1-3', '1-3'), ('3-5', '3-5'), ('5-10', '5-10'), ('10-15', '10-15'), ('15-20', '15-20'), ('20+', '20+')], max_length=16),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(default=1, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(null=True, upload_to='ing/'),
        ),
    ]
