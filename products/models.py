from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.name)


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.name)


class Unit(models.Model):
    unit = models.CharField(max_length=10)
    description = models.CharField(max_length=30)

    def __str__(self):
        return '{} - {}'.format(self.unit, self.description)


class Products(models.Model):
    name = models.CharField(max_length=50)
    cost_price = models.DecimalField(max_digits=9, decimal_places=2)
    sale_price = models.DecimalField(max_digits=9, decimal_places=2)
    icms = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    tax_substitution = models.CharField(max_length=50, null=True, blank=True)

    CTS_NFE_CHOICES = [
        ('00', 'Tributada integralmente'),
        ('10', 'Tributada e com cobrança do ICMS por substituição tributária'),
        ('20', 'Com redução da BC'),
        ('30', 'Isenta / não tributada e com cobrança do ICMS por substituição tributária'),
        ('40', 'Isenta'),
        ('41', 'Não tributada'),
        ('50', 'Com suspensão'),
        ('51', 'Com diferimento'),
        ('60', 'ICMS cobrado anteriormente por substituição tributária'),
        ('70', 'Com redução da BC e cobrança do ICMS por substituição tributária'),
        ('90', 'Outras'),
        ]
    cst_nfe = models.CharField(
        max_length=2,
        choices=CTS_NFE_CHOICES,
        default=00
    )

    ncm_nfe = models.IntegerField(null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    ORIGIN_CHOICES = [
        ('NAC', 'Nacional'),
        ('IMP', 'Importado'),
    ]
    origin = models.CharField(
        max_length=3,
        choices=ORIGIN_CHOICES,
        default='NAC'
    )

    bar_code = models.CharField(max_length=13)
    quantity = models.IntegerField()
    picture = models.ImageField(upload_to='products_photos', null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.brand)
