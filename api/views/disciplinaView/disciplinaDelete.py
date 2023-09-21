from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import DisciplinaModel
from api.serializers.disciplinaSerializer import DisciplinaSerializer  # Importa o serializador DisciplinaSerializer

class DisciplinaDelete(APIView):
    def delete(self, request, id):
        try:
            # Tenta obter um objeto DisciplinaModel com base no ID fornecido
            disciplina = DisciplinaModel.objects.get(pk=id)  
            # Deleta a disciplina do banco de dados
            disciplina.delete()  
            # Retorna uma resposta de sucesso com código 204 (No Content)
            return Response({"message": "Disciplina excluída com sucesso."}, status=status.HTTP_204_NO_CONTENT)
        # Captura a exceção caso a disciplina não seja encontrada
        except DisciplinaModel.DoesNotExist:
            return Response({"message": "Disciplina não encontrada"}, status=status.HTTP_404_NOT_FOUND)