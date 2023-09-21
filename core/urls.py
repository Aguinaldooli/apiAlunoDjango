from django.contrib import admin
from django.urls import path
from api.views.alunoView.alunoList import AlunoList
from api.views.alunoView.alunoCreate import AlunoCreate
from api.views.alunoView.alunoUpdate import AlunoUpdate
from api.views.alunoView.alunoGet import AlunoDetail
from api.views.alunoView.alunoDelete import AlunoDelete
from api.views.disciplinaView.disciplinaCreate import DisciplinaCreate
from api.views.disciplinaView.disciplinaList import DisciplinaList
from api.views.disciplinaView.disciplinaGet import DisciplinaDetail
from api.views.disciplinaView.disciplinaUpdate import DisciplinaUpdate
from api.views.disciplinaView.disciplinaDelete import DisciplinaDelete
from api.views.tarefaView.tarefaCreate import TarefaCreate
from api.views.tarefaView.tarefalist import TarefaList
from api.views.tarefaView.tarefaget import TarefaDetail
from api.views.tarefaView.tarefaupdate import TarefaUpdate
from api.views.tarefaView.tarefaDelete import TarefaDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', AlunoList.as_view()),
    path('alunos/create/', AlunoCreate.as_view()),
    path('alunos/<int:id>', AlunoDetail.as_view()),
    path('alunos/<int:id>', AlunoUpdate.as_view()),
    path('alunos/<int:pk>/delete/', AlunoDelete.as_view()),
    path('disciplinas/', DisciplinaCreate.as_view()),
    path('disciplinas/list', DisciplinaList.as_view()),
    path('disciplinas/<int:id>', DisciplinaDetail.as_view()),
    path('disciplinas/<int:id/update/', DisciplinaUpdate.as_view()),
    path('disciplinas/<int:pk>/delete/', DisciplinaDelete.as_view()),
    path('tarefa/create/', TarefaCreate.as_view()),
    path('tarefas/', TarefaList.as_view()),
    path('tarefas/<int:id>', TarefaDetail.as_view()),
    path('tarefas/<int:id>', TarefaUpdate.as_view()),
    path('tarefas/<int:pk>/delete/', TarefaDelete.as_view()),
]
