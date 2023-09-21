from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import TarefaModel

class TarefaDelete(APIView):
    def delete(self, request, id):
        try:
            # Tenta obter um objeto TarefaModel com base no ID fornecido
            tarefa = TarefaModel.objects.get(pk=id)    
            # Deleta a tarefa do banco de dados
            tarefa.delete() 
            # Retorna uma resposta de sucesso com código 204 (No Content)
            return Response({"message": "Tarefa excluída com sucesso."}, status=status.HTTP_204_NO_CONTENT)
        # Captura a exceção caso a tarefa não seja encontrada
        except TarefaModel.DoesNotExist:
            return Response({"message": "Tarefa não encontrada"}, status=status.HTTP_404_NOT_FOUND)

