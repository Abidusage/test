# Generated by Django 4.2.2 on 2023-12-13 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=50),
        ),
    ]
