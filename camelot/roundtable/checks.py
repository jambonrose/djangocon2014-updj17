# -*- coding: utf-8
from __future__ import unicode_literals
from django.apps import apps as camelot_apps
from django.core.checks import register, Warning


@register('models')
def check_model_str(app_configs=None, **kwargs):
    problem_models = [
        model
        for model in camelot_apps.get_models()
        if '__str__' not in model.__dict__
    ]
    errors = [
        Warning(
            "All Models must have a __str__ method.",
            hint=("See https://docs.djangoproject.com/"
                  "en/1.7/ref/models/instances/#str"
                  " for more information."),
            obj=model,
            id='rtable.W001',
        )
        for model in problem_models
    ]
    return errors
