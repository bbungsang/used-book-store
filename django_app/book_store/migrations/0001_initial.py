# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 10:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookBucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=48)),
                ('intro', models.TextField(blank=True)),
                ('writer', models.CharField(max_length=36)),
                ('publisher', models.CharField(max_length=36)),
                ('publication', models.CharField(max_length=12)),
                ('original_price', models.CharField(max_length=12)),
                ('used_price', models.CharField(blank=True, max_length=12)),
                ('sell_price1', models.CharField(blank=True, max_length=12)),
                ('sell_price2', models.CharField(blank=True, max_length=12)),
                ('sell_price3', models.CharField(blank=True, max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='BookLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SellBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sell_price', models.CharField(max_length=12)),
                ('book_status', models.CharField(max_length=2)),
                ('book_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_store.BookInfo')),
            ],
        ),
    ]
