# Generated by Django 4.0 on 2022-10-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board1", "0007_remove_post_subject"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="head_image",
            field=models.ImageField(blank=True, upload_to="blog/images/%Y/%m/%d"),
        ),
        migrations.AddField(
            model_name="post",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="file_upload",
            field=models.FileField(blank=True, upload_to="blog/files/%Y/%m%d"),
        ),
    ]
