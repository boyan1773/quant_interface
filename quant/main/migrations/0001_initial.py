# Generated by Django 4.2.4 on 2023-10-04 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bbc_news_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=1000)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='cnn_news_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=1000)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='yahoo_news_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=1000)),
                ('content', models.TextField()),
            ],
        ),
    ]