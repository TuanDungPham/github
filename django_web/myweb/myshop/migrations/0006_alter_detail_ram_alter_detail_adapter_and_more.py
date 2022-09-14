# Generated by Django 4.0.6 on 2022-09-02 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0005_category_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='RAM',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='detail',
            name='adapter',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='detail',
            name='battery',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='detail',
            name='chip',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='detail',
            name='front_camera',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='detail',
            name='memory',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='detail',
            name='operating_system',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='detail',
            name='rear_camera',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='detail',
            name='screen',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='detail',
            name='sim',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]