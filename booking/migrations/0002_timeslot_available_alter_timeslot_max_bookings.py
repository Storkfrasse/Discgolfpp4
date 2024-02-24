# Generated by Django 4.2.10 on 2024-02-24 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='max_bookings',
            field=models.IntegerField(default=1),
        ),
    ]