# Generated by Django 3.2.4 on 2021-07-14 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0002_rename_back_view_base_bag_productdesign_back_view_bag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='body',
            name='body_view',
        ),
    ]
