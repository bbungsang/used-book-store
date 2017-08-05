# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 03:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_store', '0006_auto_20170805_2159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookbuybucket',
            options={},
        ),
        migrations.AddField(
            model_name='bookbuybucket',
            name='transaction',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book_store.Transaction'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookcomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='댓글 작성자'),
        ),
        migrations.AlterField(
            model_name='bookcomment',
            name='content',
            field=models.TextField(verbose_name='댓글 내용'),
        ),
        migrations.AlterField(
            model_name='transactioncomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='댓글 작성자'),
        ),
        migrations.AlterField(
            model_name='transactioncomment',
            name='content',
            field=models.TextField(verbose_name='댓글 내용'),
        ),
        migrations.RemoveField(
            model_name='bookbuybucket',
            name='book',
        ),
        migrations.AlterUniqueTogether(
            name='bookbuybucket',
            unique_together=set([('user', 'transaction')]),
        ),
    ]
