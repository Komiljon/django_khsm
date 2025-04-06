from django.contrib.auth.models import User
from django.db import models


# Категории
class KhmQuestionsCategory(models.Model):    
    name = models.CharField(max_length=255, verbose_name='Сумма выигрыша', db_index=True)

    def __str__(self):
        return self.name    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"



# Вопросы
class KhmQuestions(models.Model):
    question = models.TextField(blank=True, verbose_name='Текст вопроса', null=False)
    answer_A = models.CharField(max_length=255, verbose_name='Ответ A', db_index=True)
    answer_B = models.CharField(max_length=255, verbose_name='Ответ B', db_index=True)
    answer_C = models.CharField(max_length=255, verbose_name='Ответ C', db_index=True)
    answer_D = models.CharField(max_length=255, verbose_name='Ответ D', db_index=True)
    trueanswer = models.CharField(max_length=255, verbose_name='Вариант правильного ответа', db_index=True)
    clue1 = models.TextField(blank=True, verbose_name='Подсказка для ведущего о произношении', null=False)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания', db_index=True)
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения', db_index=True)
    is_published = models.BooleanField(default=True, verbose_name='Публикация', db_index=True)    
    cat = models.ForeignKey('KhmQuestionsCategory', verbose_name='Категория', on_delete=models.PROTECT, null=False, db_index=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, db_index=True)
    
    def __str__(self):
        return self.question    
    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
