from django.contrib import admin
from trainapp.models import TrainApp, TrainAppCategory

admin.site.register(TrainAppCategory)
admin.site.register(TrainApp)