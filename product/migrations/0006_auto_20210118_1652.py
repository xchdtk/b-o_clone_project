# Generated by Django 3.1.4 on 2021-01-18 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210118_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='video_url',
        ),
        migrations.AlterField(
            model_name='feature',
            name='image_url',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='inspiration',
            name='slide_image_url',
            field=models.TextField(),
        ),
    ]
