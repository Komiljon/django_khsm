from django.contrib.auth.models import User
from django.db import models


# Категории
class TrainAppCategory(models.Model):    
    name = models.CharField(max_length=255, verbose_name='Категории расписаний', db_index=True)

    def __str__(self):
        return self.name    
    class Meta:
        verbose_name = "Категория расписания"
        verbose_name_plural = "Категории расписаний"



# Вопросы
class TrainApp(models.Model):
    rasp = models.TextField(blank=True, verbose_name='Расписание', null=False)
    
    
    def __str__(self):
        return self.rasp    
    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписании"
