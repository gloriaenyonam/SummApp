# Generated by Django 3.2 on 2023-05-12 15:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APPUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('signup_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ('-signup_date', '-id'),
            },
        ),
    ]
