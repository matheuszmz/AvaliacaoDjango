# Generated by Django 3.0.5 on 2020-05-01 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200501_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='profit_percentage',
        ),
        migrations.AlterField(
            model_name='products',
            name='cst_nfe',
            field=models.CharField(choices=[('00', 'Tributada integralmente'), ('10', 'Tributada e com cobrança do ICMS por substituição tributária'), ('20', 'Com redução da BC'), ('30', 'Isenta / não tributada e com cobrança do ICMS por substituição tributária'), ('40', 'Isenta'), ('41', 'Não tributada'), ('50', 'Com suspensão'), ('51', 'Com diferimento'), ('60', 'ICMS cobrado anteriormente por substituição tributária'), ('70', 'Com redução da BC e cobrança do ICMS por substituição tributária'), ('90', 'Outras')], default=0, max_length=2),
        ),
    ]
