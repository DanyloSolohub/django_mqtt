# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-19 00:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_mqtt.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ACL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow', models.BooleanField(default=True)),
                ('acc', models.IntegerField(choices=[(1, 'Suscriptor'), (2, 'Publisher')])),
                ('password', models.CharField(blank=True, help_text='Only valid for connect', max_length=512, null=True)),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='ClientId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=23, unique=True, validators=[django_mqtt.validators.ClientIdValidator(valid_empty=False)])),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=1024, unique=True, validators=[django_mqtt.validators.TopicValidator()])),
                ('wildcard', models.BooleanField(default=False)),
                ('dollar', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='acl',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_mqtt.Topic'),
        ),
        migrations.AddField(
            model_name='acl',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='acl',
            unique_together=set([('topic', 'acc')]),
        ),
    ]
