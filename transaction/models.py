from django.db import models

class Transaction(models.Model):
    operator = models.CharField(max_length=64)
    phone = models.CharField(max_length=13)
    date = models.DateTimeField(auto_now_add=True)
    sum = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        return f'{self.pk}'
