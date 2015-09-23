from django.db import models
from django.utils.timezone import now


class Movement(models.Model):
    account = models.CharField(max_length=255)
    date = models.DateField(default=now)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8,
                                 decimal_places=2)
