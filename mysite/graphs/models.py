from django.db import models

# Create your models here.


class Gene(models.Model):
    gene_symbol = models.CharField(max_length=100)
    control1 = models.DecimalField(max_digits=8, decimal_places=5)
    control2 = models.DecimalField(max_digits=8, decimal_places=5)
    control3 = models.DecimalField(max_digits=8, decimal_places=5)
    control4 = models.DecimalField(max_digits=8, decimal_places=5)
    control5 = models.DecimalField(max_digits=8, decimal_places=5)
    kras1 = models.DecimalField(max_digits=8, decimal_places=5)
    kras2 = models.DecimalField(max_digits=8, decimal_places=5)
    kras3 = models.DecimalField(max_digits=8, decimal_places=5)
    kras4 = models.DecimalField(max_digits=8, decimal_places=5)
    kras5 = models.DecimalField(max_digits=8, decimal_places=5)
