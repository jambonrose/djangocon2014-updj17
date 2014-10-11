# -*- coding: utf-8
from __future__ import unicode_literals
from django.apps import AppConfig
from django.core.checks import register
from .checks import check_model_str


class RoundtableConfig(AppConfig):
    name = 'roundtable'
    label = 'rtable'
    verbose_name = 'Round Table'

    def ready(self):
        super(RoundtableConfig, self).ready()
        register('models')(check_model_str)
