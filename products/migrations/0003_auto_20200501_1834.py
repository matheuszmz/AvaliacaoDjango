# Generated by Django 3.0.5 on 2020-05-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200501_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='bar_code',
            field=models.CharField(max_length=13),
        ),
    ]