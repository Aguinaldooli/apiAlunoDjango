from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import DisciplinaModel
from api.serializers.disciplinaSerializer import DisciplinaSerializer  

class DisciplinaDetail(APIView):
    def get(self, request, id):
        try:
            # Tenta obter um objeto DisciplinaModel com base no ID fornecido
            disciplina = DisciplinaModel.objects.get(pk=id)    
            # Cria um objeto de serializador DisciplinaSerializer com base no objeto disciplina
            serializer = DisciplinaSerializer(disciplina)     
            # Retorna uma resposta com os dados serializados da disciplina com código 200 (OK)
            return Response(serializer.data, status=status.HTTP_200_OK) 
        # Captura a exceção caso a disciplina não seja encontrada
        except DisciplinaModel.DoesNotExist:
            return Response({"message": "Disciplina não encontrada"}, status=status.HTTP_404_NOT_FOUND)