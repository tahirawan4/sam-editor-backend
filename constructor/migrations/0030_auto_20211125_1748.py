# Generated by Django 3.2.4 on 2021-11-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0029_userorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_no',
            field=models.TextField(blank=True, null=True),
        ),
    ]
