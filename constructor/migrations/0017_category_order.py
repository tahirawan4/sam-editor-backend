# Generated by Django 3.2.4 on 2021-07-03 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0016_alter_body_left_sleeve'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]