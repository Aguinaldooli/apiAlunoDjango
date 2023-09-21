from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import DisciplinaModel
from api.serializers.disciplinaSerializer import DisciplinaSerializer  # Importa o serializador DisciplinaSerializer

class DisciplinaList(APIView):
    def get(self, request):
        try:
            # Obtém todas as disciplinas do banco de dados
            disciplinas = DisciplinaModel.objects.all()           
            # Cria um objeto de serializador DisciplinaSerializer com base na lista de disciplinas
            serializer = DisciplinaSerializer(disciplinas, many=True)      
            # Retorna uma resposta com os dados serializados das disciplinas com código 200 (OK)
            return Response(serializer.data, status=status.HTTP_200_OK)   
        # Captura exceções gerais e retorna uma resposta de erro com código 500 (Internal Server Error)
        except Exception as e:
            return Response({"message": "Erro ao listar disciplinas: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)