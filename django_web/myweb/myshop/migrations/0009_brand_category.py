# Generated by Django 4.0.6 on 2022-09-03 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0008_alter_detail_memory'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myshop.category'),
        ),
    ]
