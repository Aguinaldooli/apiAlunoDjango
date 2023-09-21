from django.db import models
from api.models import AlunoModel
from api.models import DisciplinaModel

class TarefaModel(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_entrega = models.DateField()
    concluida = models.BooleanField(default=False)
    aluno = models.ForeignKey(AlunoModel, on_delete=models.CASCADE, related_name='tarefas')
    disciplinas = models.ManyToManyField(DisciplinaModel, related_name='tarefas')

    def __str__(self):
        return self.titulo