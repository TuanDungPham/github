# Generated by Django 4.0.6 on 2022-07-24 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_delete_article_delete_publication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Publication',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('publications', models.ManyToManyField(to='myapp.publication')),
            ],
            options={
                'db_table': 'Article',
                'ordering': ['headline'],
            },
        ),
    ]
