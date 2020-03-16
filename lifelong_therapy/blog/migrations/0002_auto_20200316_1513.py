# Generated by Django 3.0.4 on 2020-03-16 15:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_content',
            field=ckeditor.fields.RichTextField(default='empty'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]
