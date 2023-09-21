from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import TarefaModel
from api.serializers.tarefaSerializer import TarefaSerializer  # Importa o serializador TarefaSerializer

class TarefaCreate(APIView):
    def post(self, request):
        # Cria um objeto de serializador TarefaSerializer com base nos dados da solicitação
        serializer = TarefaSerializer(data=request.data)
        # Verifica se os dados enviados na solicitação são válidos de acordo com o serializador
        if serializer.is_valid():
            # Salva a nova tarefa no banco de dados
            serializer.save()         
            # Retorna uma resposta com os dados serializados da tarefa criada com código 201 (Created)
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        # Se os dados não forem válidos, retorna uma resposta com os erros de validação com código 400 (Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)