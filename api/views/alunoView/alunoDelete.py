from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.response import Response
from api.models import AlunoModel
from api.serializers.alunoSerializer import AlunoSerializer

class AlunoDelete(APIView):
    def get(self, request, pk):
        try:
            # Tenta obter um objeto AlunoModel com base no ID fornecido
            aluno = AlunoModel.objects.get(pk=pk)
            # Cria um objeto de serializador AlunoSerializer com base no objeto aluno
            serializer = AlunoSerializer(aluno)
            # Retorna uma resposta com os dados serializados do aluno com código 200 (OK)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # Captura a exceção caso o aluno não seja encontrado
        except AlunoModel.DoesNotExist:
            return Response({"message": "Aluno não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            # Tenta obter um objeto AlunoModel com base no ID fornecido
            aluno = AlunoModel.objects.get(pk=pk)
            # Deleta o aluno do banco de dados
            aluno.delete()
            # Retorna uma resposta de sucesso com código 204 (No Content)
            return Response({"message": "Aluno excluído com sucesso."}, status=status.HTTP_204_NO_CONTENT)
        # Captura a exceção caso o aluno não seja encontrado
        except AlunoModel.DoesNotExist:
            return Response({"message": "Aluno não encontrado"}, status=status.HTTP_404_NOT_FOUND)