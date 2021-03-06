# Generated by Django 3.0.2 on 2021-07-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title ')),
                ('name', models.CharField(max_length=50, verbose_name='Name ')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=70, verbose_name='Phone')),
                ('address', models.CharField(max_length=70, verbose_name='Address')),
            ],
            options={
                'verbose_name': 'customer order',
                'verbose_name_plural': 'customer orders',
                'db_table': 'customer_orders',
                'managed': True,
            },
        ),
    ]
