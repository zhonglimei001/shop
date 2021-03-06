# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'shop_category',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('value', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'shop_color',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=255)),
                ('gdesc', models.CharField(blank=True, max_length=1024, null=True)),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('goldprice', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'shop_goods',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Goodsdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'shop_goodsdetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'shop_size',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'shop_store',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StoreSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'shop_store_size',
                'managed': False,
            },
        ),
    ]
