from django.db import models
from persons.models import PersonAbstract



# Create your models here.
class Studentshelper(PersonAbstract):
    subjects = models.TextField(verbose_name='Предмет(ы)')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

        ordering = ['first_name', 'last_name', 'subjects']

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.subjects}'


