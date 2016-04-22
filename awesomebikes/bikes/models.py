from django.db import models


class Bike(models.Model):
    model_name = models.CharField(max_length=255, null=True, blank=True)
    size = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    data_bought = models.DateTimeField(null=True, blank=True)
