# Generated by Django 3.2.4 on 2021-07-08 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0022_auto_20210708_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='apron',
            name='display_image',
            field=models.ImageField(default='', upload_to='uploads/display'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='towel',
            name='display_image',
            field=models.ImageField(default=1, upload_to='uploads/display'),
            preserve_default=False,
        ),
    ]