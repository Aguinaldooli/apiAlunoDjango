from django.contrib import admin
from django.urls import path
from api.views.alunoView.alunoList import AlunoList
from api.views.alunoView.alunoCreate import AlunoCreate
from api.views.alunoView.alunoUpdate import AlunoUpdate
from api.views.alunoView.alunoGet import AlunoDetail
from api.views.alunoView.alunoDelete import AlunoDelete
from api.views.disciplinaView.disciplinaCreate import DisciplinaCreate
from api.views.disciplinaView.disciplinaList import DisciplinaList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', AlunoList.as_view()),
    path('alunos/create/', AlunoCreate.as_view()),
    path('alunos/<int:id>', AlunoDetail.as_view()),
    path('alunos/<int:id>', AlunoUpdate.as_view()),
    path('alunos/<int:pk>/delete/', AlunoDelete.as_view()),
    path('disciplinas/', DisciplinaCreate.as_view()),
    path('disciplinas/', DisciplinaList.as_view()),
]
