# Generated by Django 3.0.6 on 2020-07-13 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BTTVapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='path_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
