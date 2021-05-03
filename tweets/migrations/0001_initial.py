# Generated by Django 3.2 on 2021-04-26 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Tweet',
                'verbose_name_plural': 'Tweets',
            },
        ),
    ]