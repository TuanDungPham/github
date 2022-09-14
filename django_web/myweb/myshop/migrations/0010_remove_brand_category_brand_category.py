# Generated by Django 4.0.6 on 2022-09-03 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0009_brand_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='category',
        ),
        migrations.AddField(
            model_name='brand',
            name='category',
            field=models.ManyToManyField(to='myshop.category'),
        ),
    ]
