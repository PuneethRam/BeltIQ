# Generated by Django 4.2.9 on 2024-04-20 11:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_product_api_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='api_key',
        ),
        migrations.AddField(
            model_name='product',
            name='info',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
