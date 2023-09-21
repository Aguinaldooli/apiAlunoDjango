from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import TarefaModel
from api.serializers.tarefaSerializer import TarefaSerializer  

class TarefaList(APIView):
    def get(self, request):
        try:
            # Obtém todas as tarefas do banco de dados
            tarefas = TarefaModel.objects.all()
            # Cria um objeto de serializador TarefaSerializer com base na lista de tarefas
            serializer = TarefaSerializer(tarefas, many=True)
            # Retorna uma resposta com os dados serializados das tarefas com código 200 (OK)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # Captura exceções gerais e retorna uma resposta de erro com código 500 (Internal Server Error)
        except Exception as e:
            return Response({"message": "Erro ao listar tarefas: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)