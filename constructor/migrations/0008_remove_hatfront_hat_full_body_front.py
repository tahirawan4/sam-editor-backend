# Generated by Django 3.2.4 on 2021-07-14 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0007_remove_apron_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hatfront',
            name='hat_full_body_front',
        ),
    ]
