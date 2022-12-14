# Generated by Django 4.0.6 on 2022-08-28 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_parent',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='product',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderDetail',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
        migrations.DeleteModel(
            name='Promotion',
        ),
    ]
