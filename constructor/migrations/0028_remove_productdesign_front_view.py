# Generated by Django 3.2.4 on 2021-07-13 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0027_alter_productdesign_front_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdesign',
            name='front_view',
        ),
    ]