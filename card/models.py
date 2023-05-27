from django.db import models
from django.core.validators import MaxValueValidator

class Card(models.Model):
    number = models.IntegerField(validators=[MaxValueValidator(9999999999999999)])
    balance = models.CharField(max_length=6)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=2)
    cvv = models.IntegerField(validators=[MaxValueValidator(999)])

    def __str__(self):
        return f'{self.pk}'
