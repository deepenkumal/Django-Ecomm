# Generated by Django 3.1.5 on 2021-05-10 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Product Name')),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('category', models.CharField(max_length=150, verbose_name='Product Category')),
                ('description', models.TextField(verbose_name='Product Description')),
                ('image', models.CharField(max_length=150)),
            ],
        ),
    ]
