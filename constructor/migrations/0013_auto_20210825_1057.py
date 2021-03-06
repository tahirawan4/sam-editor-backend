# Generated by Django 3.2.4 on 2021-08-25 10:57

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0012_auto_20210811_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Color Name', max_length=250, unique=True)),
                ('color_code', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Fabric Name', max_length=250, unique=True)),
                ('short_description', models.CharField(blank=True, help_text='Short Description', max_length=250, null=True)),
                ('colors', models.ManyToManyField(to='constructor.Color')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='productdesign',
            name='fabrics',
            field=models.ManyToManyField(to='constructor.Color'),
        ),
    ]
