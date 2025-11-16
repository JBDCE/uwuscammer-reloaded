from django.db import models

# Create your models here.
class CreditCard(models.Model):
    # TODO Figure out if this is large enough for this feature
    cardnum = models.BigIntegerField(max_length=16)
    expiry = models.DateField()
    cvs = models.IntegerField(max_length=3)
