# Generated by Django 3.2.16 on 2023-11-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khm_questions', '0002_auto_20231114_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='khmquestions',
            name='clue1',
            field=models.TextField(blank=True, verbose_name='Подсказка для ведущего о произношении'),
        ),
    ]
