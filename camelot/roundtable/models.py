# -*- coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.core.checks import Error
from django.utils.encoding import python_2_unicode_compatible


class KnightQuerySet(models.QuerySet):
    def dances_when_able(self):
        return self.filter(dances=True)

    def loyal(self):
        return self.filter(traitor=False)


@python_2_unicode_compatible
class Knight(models.Model):
    name = models.CharField(max_length=63)
    traitor = models.BooleanField(default=False)
    dances = models.BooleanField(default=True)

    objects = KnightQuerySet.as_manager()

    def __str__(self):
        return self.name

    @classmethod
    def check(cls, **kwargs):
        errors = super(Knight, cls).check(**kwargs)
        errors.extend(cls._check_traitor_field(**kwargs))
        return errors

    @classmethod
    def _check_traitor_field(cls, **kwargs):
        if 'traitor' not in cls._meta.get_all_field_names():
            return [
                Error(
                    "Knight model must have a traitor field.",
                    obj=cls,
                    id='rtable.E001')]
        else:
            return []
