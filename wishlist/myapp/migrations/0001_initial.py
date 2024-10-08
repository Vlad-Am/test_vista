# Generated by Django 5.1 on 2024-08-28 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyWishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Цена')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Ссылка')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Примечание')),
            ],
        ),
    ]
