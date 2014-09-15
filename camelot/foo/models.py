from django.db import models


class Bar(models.Model):
    name = models.CharField(max_length=31)
