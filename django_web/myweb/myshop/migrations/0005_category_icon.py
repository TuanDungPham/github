# Generated by Django 4.0.6 on 2022-09-01 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_alter_detail_ram_alter_detail_adapter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.TextField(blank=True),
        ),
    ]
