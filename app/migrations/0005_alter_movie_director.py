# Generated by Django 3.2 on 2022-01-12 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220112_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
