# Generated by Django 4.0 on 2022-10-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address1',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='address2',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='zipcode',
            field=models.IntegerField(blank=True),
        ),
    ]
