# Generated by Django 4.2.9 on 2024-04-20 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_remove_product_api_key_product_info_product_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeltAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_status', models.CharField(max_length=100)),
                ('location', models.CharField(default='', max_length=1000)),
                ('reason', models.CharField(default='', max_length=1000)),
                ('measure', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
