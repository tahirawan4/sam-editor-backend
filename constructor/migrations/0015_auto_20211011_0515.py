# Generated by Django 3.2.4 on 2021-10-11 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0014_alter_productdesign_fabrics'),
    ]

    operations = [
        migrations.CreateModel(
            name='DigitalPrintingMethodSizeCostQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
                ('cost', models.FloatField(default=0)),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HeatTransferPrintingMethodSizeCostQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('printing_type', models.CharField(choices=[('color_printing', 'Color Printing'), ('3m_reflective', '3M Reflective'), ('metal', 'Metal')], max_length=50, unique=True)),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
                ('cost', models.FloatField(default=0)),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SilkPrintingMethodSizeCostQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Fabric Name', max_length=250, unique=True)),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
                ('quantity_to', models.IntegerField()),
                ('quantity_from', models.IntegerField()),
                ('standard_cost', models.FloatField(default=0)),
                ('custom_cost', models.FloatField(default=0)),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SizeFieldModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='fabric',
            name='cost',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='ProductSizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Product Size Name', max_length=250)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.sizefieldmodel')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrintingMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('printing_method', models.CharField(choices=[('silk_screen', 'Silk Screen Printing'), ('heat_transfer', 'Heat Transfer Printing'), ('digital', 'Digital Printing')], default='silk_screen', max_length=50)),
                ('name', models.CharField(help_text='Printing Method Name', max_length=250, unique=True)),
                ('digital_sizes_cost', models.ManyToManyField(to='constructor.DigitalPrintingMethodSizeCostQuantity')),
                ('heat_transfer_sizes_cost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.heattransferprintingmethodsizecostquantity')),
                ('silk_sizes_quantity_cost', models.ManyToManyField(to='constructor.SilkPrintingMethodSizeCostQuantity')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='productdesign',
            name='printing_method',
            field=models.ManyToManyField(to='constructor.PrintingMethod'),
        ),
        migrations.AddField(
            model_name='productdesign',
            name='sizes',
            field=models.ManyToManyField(to='constructor.ProductSizeModel'),
        ),
    ]
