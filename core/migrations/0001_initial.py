# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-13 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of information.', max_length=100, verbose_name='Title')),
                ('image', models.ImageField(blank=True, help_text='Image about information.', null=True, upload_to='news', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date of creation of information', verbose_name='Created at')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link of information')),
                ('content', models.TextField(verbose_name='Description')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identify')),
            ],
            options={
                'verbose_name': 'News',
                'ordering': ('created_at', 'title'),
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Tag')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identify')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', related_query_name='tags', to='core.Tag'),
        ),
    ]