# -*- coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Knight(models.Model):
    name = models.CharField(max_length=63)
    traitor = models.BooleanField()

    def __str__(self):
        return self.name
