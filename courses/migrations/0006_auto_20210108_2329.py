# Generated by Django 3.1.5 on 2021-01-08 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20210108_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
