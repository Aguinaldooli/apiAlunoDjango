from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models.disciplinaModel import DisciplinaModel  
from api.serializers.disciplinaSerializer import DisciplinaSerializer 


class DisciplinaCreate(APIView):
    # Função para criar uma nova disciplina via solicitação POST
    def post(self, request):
        # Cria um serializador DisciplinaSerializer com os dados da solicitação
        serializer = DisciplinaSerializer(data=request.data)

        # Verifica se os dados fornecidos são válidos de acordo com o serializador
        if serializer.is_valid():
            # Salva a nova disciplina no banco de dados
            serializer.save()

            # Retorna uma resposta de sucesso com os dados da disciplina criada e o status 201 CREATED
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Se os dados não forem válidos, retorna uma resposta de erro com detalhes dos erros
            # de validação e o status 400 BAD REQUEST
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)