# Generated by Django 2.0.2 on 2018-04-03 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180403_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hifz',
            name='last_refreshed',
            field=models.DateTimeField(),
        ),
    ]
