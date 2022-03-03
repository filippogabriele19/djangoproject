from django.conf import settings
from django.db import models
from django.utils import timezone
from string import ascii_uppercase, digits
from .utils import sendTransaction
import hashlib
from django.db.models.signals import post_save
from random import choice


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    code = models.CharField(max_length=10)
    creation_date = models.DateTimeField(default=timezone.now)
    transactionid = models.TextField(default="")

    def save(self, *args, **kwargs):
        self.code = "".join(choice(ascii_uppercase + digits) for i in range(10))
        hash = hashlib.sha256(
            (str(self.description) + "-" + self.code).encode("utf-8")
        ).hexdigest()
        self.transactionid = sendTransaction(hash)
        super(Product, self).save(*args, **kwargs)


class Lastip(models.Model):
    ip = models.CharField(max_length=200)


class StepProduct(models.Model):
    description = models.TextField()
    code = models.CharField(max_length=10)
    creation_date = models.DateTimeField(default=timezone.now)
