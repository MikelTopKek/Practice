from django.db import models


class Numeric(models.Model):
    value = models.CharField(max_length=64)
    type = models.BooleanField(default=0)
