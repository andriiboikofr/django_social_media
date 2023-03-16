# Generated by Django 4.1.7 on 2023-03-14 16:48

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('7a7221a2-2ad0-43ce-876e-d60e0773818a'), primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post_images')),
                ('caption', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 3, 14, 16, 48, 38, 907558))),
                ('no_of_likes', models.IntegerField(default=0)),
            ],
        ),
    ]