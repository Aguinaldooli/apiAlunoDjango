from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import AlunoModel
from api.serializers.alunoSerializer import AlunoSerializer

class AlunoDetail(APIView):
    def get(self, request, id):
        try:
            # Tenta buscar um objeto AlunoModel no banco de dados com base no ID fornecido
            aluno = AlunoModel.objects.get(pk=id)
            serializer = AlunoSerializer(aluno)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AlunoModel.DoesNotExist:
            return Response({"Aluno não encontrado"}, status=status.HTTP_404_NOT_FOUND)