# -*- coding: utf-8
from __future__ import unicode_literals
from django.core.checks import register


@register('models')
def check_model_str(app_configs=None, **kwargs):
    errors = [
    ]
    return errors
