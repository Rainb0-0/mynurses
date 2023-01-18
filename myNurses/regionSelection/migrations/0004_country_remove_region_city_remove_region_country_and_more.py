# Generated by Django 4.1.5 on 2023-01-18 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regionSelection', '0003_alter_region_city_alter_region_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countryName', models.CharField(help_text='The country name', max_length=200, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='region',
            name='city',
        ),
        migrations.RemoveField(
            model_name='region',
            name='country',
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityName', models.CharField(help_text='The city name', max_length=200, unique=True)),
                ('countryName', models.ManyToManyField(to='regionSelection.country')),
            ],
        ),
        migrations.AddField(
            model_name='region',
            name='cityName',
            field=models.ManyToManyField(to='regionSelection.city'),
        ),
    ]