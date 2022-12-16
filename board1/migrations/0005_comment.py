# Generated by Django 4.0 on 2022-10-26 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_zipcode'),
        ('board1', '0004_alter_post_options_post_file_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board1_my_author_set', to='accounts.user')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board1.post')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
