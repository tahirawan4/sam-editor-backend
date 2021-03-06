# Generated by Django 3.2.4 on 2021-07-14 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0009_auto_20210714_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vestfront',
            name='vest_bottom_left',
        ),
        migrations.RemoveField(
            model_name='vestfront',
            name='vest_bottom_right',
        ),
        migrations.RemoveField(
            model_name='vestfront',
            name='vest_mid_left',
        ),
        migrations.RemoveField(
            model_name='vestfront',
            name='vest_mid_right',
        ),
        migrations.RemoveField(
            model_name='vestfront',
            name='vest_top_full',
        ),
        migrations.RemoveField(
            model_name='vestfront',
            name='vest_top_left',
        ),
        migrations.RemoveField(
            model_name='vestfront',
            name='vest_top_right',
        ),
        migrations.AddField(
            model_name='vestfront',
            name='vest_bottom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vest_bottom', to='constructor.imagefield'),
        ),
        migrations.AddField(
            model_name='vestfront',
            name='vest_mid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vest_mid', to='constructor.imagefield'),
        ),
        migrations.AddField(
            model_name='vestfront',
            name='vest_top',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vest_top', to='constructor.imagefield'),
        ),
    ]
