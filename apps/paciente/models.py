from django.db import models

# Create your models here.

class Paciente(models.Model):
    nome = models.CharField('nome', max_length=40)
    
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Paciente'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.name}'