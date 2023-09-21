from django.db import models

class DisciplinaModel(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.TextField()

    def __str__(self):
        return self.nome