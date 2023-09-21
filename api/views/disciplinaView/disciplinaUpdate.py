from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import DisciplinaModel
from api.serializers.disciplinaSerializer import DisciplinaSerializer  # Importa o serializador DisciplinaSerializer

class DisciplinaUpdate(APIView):
    def put(self, request, id):
        try:
            # Tenta obter um objeto DisciplinaModel com base no ID fornecido
            disciplina = DisciplinaModel.objects.get(pk=id)
            # Cria um objeto de serializador DisciplinaSerializer com base no objeto disciplina e nos dados da solicitação
            serializer = DisciplinaSerializer(disciplina, data=request.data) 
            # Verifica se os dados enviados na solicitação são válidos de acordo com o serializador
            if serializer.is_valid():
                # Salva as alterações no objeto disciplina
                serializer.save() 
                # Retorna uma resposta com os dados serializados atualizados com código 200 (OK)
                return Response(serializer.data, status=status.HTTP_200_OK)     
            # Se os dados não forem válidos, retorna uma resposta com os erros de validação com código 400 (Bad Request)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
        # Captura a exceção caso a disciplina não seja encontrada
        except DisciplinaModel.DoesNotExist:
            return Response({"message": "Disciplina não encontrada"}, status=status.HTTP_404_NOT_FOUND)