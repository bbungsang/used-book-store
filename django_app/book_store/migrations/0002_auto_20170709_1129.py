# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 11:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book_store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='sellbook',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='book_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_store.BookInfo'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booklike',
            name='book_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_store.BookInfo'),
        ),
        migrations.AddField(
            model_name='booklike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='book_bucket',
            field=models.ManyToManyField(related_name='book_bucket', through='book_store.BookBucket', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='book_like',
            field=models.ManyToManyField(related_name='like_books', through='book_store.BookLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookbucket',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_store.BookInfo'),
        ),
        migrations.AddField(
            model_name='bookbucket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
