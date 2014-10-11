# -*- coding: utf-8
from __future__ import unicode_literals
from django.apps import apps as camelot_apps
from django.core.checks import register, Tags, Warning


@register(Tags.models)
def check_model_str(app_configs=None, **kwargs):
    problem_models = [
        model
        for model in camelot_apps.get_models()
        if (app_configs is None
            or model._meta.app_config in app_configs)
        and not model._meta.app_config.name.startswith(
            'django.contrib')
        and '__str__' not in model.__dict__
    ]
    errors = [
        Warning(
            "All Models must have a __str__ method.",
            hint=("See https://docs.djangoproject.com/"
                  "en/1.7/ref/models/instances/#str"
                  " for more information."),
            obj=model,
            id='camelot.W001',
        )
        for model in problem_models
    ]
    return errors
