# Generated by Django 4.0.6 on 2022-09-03 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0007_alter_detail_ram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='memory',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]