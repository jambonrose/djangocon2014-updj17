# -*- coding: utf-8
from __future__ import unicode_literals
from django.db import models

class Knight(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name
