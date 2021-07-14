# Generated by Django 3.2.4 on 2021-07-10 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0024_vestback_vestfront'),
    ]

    operations = [
        migrations.CreateModel(
            name='PantFront',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Pant Front', max_length=250)),
                ('pant_bottom_left_front', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_bottom_left_front', to='constructor.imagefield')),
                ('pant_bottom_right_front', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_bottom_right_front', to='constructor.imagefield')),
                ('pant_knees_left_front', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_knees_left_front', to='constructor.imagefield')),
                ('pant_knees_right_front', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_knees_right_front', to='constructor.imagefield')),
                ('pant_lower_waist_front', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_lower_waist_front', to='constructor.imagefield')),
                ('pant_pocket_left_front', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_pocket_left_front', to='constructor.imagefield')),
                ('pant_pocket_right_front', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_pocket_right_front', to='constructor.imagefield')),
                ('pant_thai_left_front', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_thai_left_front', to='constructor.imagefield')),
                ('pant_thai_right_front', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_thai_right_front', to='constructor.imagefield')),
                ('pant_upper_waist_front', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_upper_waist_front', to='constructor.imagefield')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
            },
        ),
        migrations.CreateModel(
            name='PantBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Pant Back', max_length=250)),
                ('pant_bottom_left_back', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_bottom_left_back', to='constructor.imagefield')),
                ('pant_bottom_right_back', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_bottom_right_back', to='constructor.imagefield')),
                ('pant_knees_left_back', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_knees_left_back', to='constructor.imagefield')),
                ('pant_knees_right_back', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_knees_right_back', to='constructor.imagefield')),
                ('pant_lower_waist_back', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_lower_waist_back', to='constructor.imagefield')),
                ('pant_pocket_left_back', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_pocket_left_back', to='constructor.imagefield')),
                ('pant_pocket_right_back', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_pocket_right_back', to='constructor.imagefield')),
                ('pant_thai_left_back', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_thai_left_back', to='constructor.imagefield')),
                ('pant_thai_right_back', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_thai_right_back', to='constructor.imagefield')),
                ('pant_upper_waist_back', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pant_upper_waist_back', to='constructor.imagefield')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
            },
        ),
    ]
