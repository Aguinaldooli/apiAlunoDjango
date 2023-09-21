from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import TarefaModel
from api.serializers.tarefaSerializer import TarefaSerializer  
class TarefaDetail(APIView):
    def get(self, request, id):
        try:
            # Tenta obter um objeto TarefaModel com base no ID fornecido
            tarefa = TarefaModel.objects.get(pk=id)
            # Cria um objeto de serializador TarefaSerializer com base no objeto tarefa
            serializer = TarefaSerializer(tarefa)
            # Retorna uma resposta com os dados serializados da tarefa com código 200 (OK)
            return Response(serializer.data, status=status.HTTP_200_OK)  
        # Cptura a exceção caso a tarefa não seja encontrada
        except TarefaModel.DoesNotExist:
            return Response({"message": "Tarefa não encontrada"}, status=status.HTTP_404_NOT_FOUND)