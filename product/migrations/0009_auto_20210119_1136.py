# Generated by Django 3.1.4 on 2021-01-19 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20210119_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspiration',
            name='slide_image_url',
            field=models.JSONField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspiration',
            name='video_url',
            field=models.JSONField(default=1),
            preserve_default=False,
        ),
    ]
