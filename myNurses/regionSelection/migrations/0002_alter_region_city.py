# Generated by Django 4.1.5 on 2023-01-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regionSelection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='city',
            field=models.CharField(choices=[('Tehran', 'Tehran'), ('kerman', 'kerman')], help_text='regions city', max_length=200),
        ),
    ]
