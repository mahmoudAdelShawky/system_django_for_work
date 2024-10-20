from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models import CASCADE

# Create your models here.
class Product (models.Model):
    user = models.ForeignKey(User , on_delete=CASCADE)
    name = models.CharField(max_length=50)
    quantaty = models.DecimalField(max_digits=10, decimal_places=1, default=True)
    package_weight = models.DecimalField(max_digits=10, decimal_places=1, default=True)
    created = models.DateTimeField(blank=True, default=datetime.datetime.now())
    notes = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name