# Generated by Django 4.2.4 on 2023-08-04 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satellite_monitoring', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satellites',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]
