# Generated by Django 3.0.4 on 2020-04-02 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='appointment_time',
        ),
        migrations.AlterField(
            model_name='patient',
            name='appointment_date',
            field=models.DateTimeField(verbose_name='date appointed'),
        ),
    ]
