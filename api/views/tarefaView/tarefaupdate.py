from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import TarefaModel
from api.serializers.tarefaSerializer import TarefaSerializer  

class TarefaUpdate(APIView):
    def put(self, request, id):
        try:
            # Tenta obter um objeto TarefaModel com base no ID fornecido
            tarefa = TarefaModel.objects.get(pk=id)
            # Cria um objeto de serializador TarefaSerializer com base no objeto tarefa e nos dados da solicitação
            serializer = TarefaSerializer(tarefa, data=request.data)
            # Verifica se os dados enviados na solicitação são válidos de acordo com o serializador
            if serializer.is_valid():
                # Salva as alterações no objeto tarefa
                serializer.save()
                # Retorna uma resposta com os dados serializados atualizados com código 200 (OK)
                return Response(serializer.data, status=status.HTTP_200_OK)
            # Se os dados não forem válidos, retorna uma resposta com os erros de validação com código 400 (Bad Request)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Captura a exceção caso a tarefa não seja encontrada
        except TarefaModel.DoesNotExist:
            return Response({"message": "Tarefa não encontrada"}, status=status.HTTP_404_NOT_FOUND)