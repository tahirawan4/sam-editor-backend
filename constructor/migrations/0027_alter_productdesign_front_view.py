# Generated by Django 3.2.4 on 2021-07-12 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0026_bagback_bagfront_baseballjacket_back_baseballjacket_front_baseballjacket_left_baseballjacket_right_b'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdesign',
            name='front_view',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.apron'),
        ),
    ]