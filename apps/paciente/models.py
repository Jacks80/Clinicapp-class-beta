from django.db import models

# Create your models here.

class Paciente(models.Model):
    id_paciente = models.IntegerField('id_paciente')
    nome = models.CharField('nome', max_length=40)
    cpf = models.CharField('cpf',max_length=11)
    telefone = models.CharField('telefone',max_length=9)
    endereco = models.CharField('endereço',max_length=40)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['id']

    def __str__(self):
        return f'(self.id) - {self.name}'