# Generated by Django 3.0.7 on 2020-06-30 23:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_contentTR',
            field=ckeditor.fields.RichTextField(blank=True, default='Türkçesi henüz eklenmedi'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_headerTR',
            field=models.CharField(default='Türkçesi henüz eklenmedi', max_length=200),
        ),
    ]