from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import AlunoModel
from api.serializers.alunoSerializer import AlunoSerializer

class AlunoList(APIView):
    def get(self, request):
        try:
            # Tenta buscar todos os objetos AlunoModel no banco de dados
            alunos = AlunoModel.objects.all()
            serializer = AlunoSerializer(alunos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            # Se ocorrer uma exceção (erro), retorna uma resposta HTTP 500 (Internal Server Error)
            # com uma mensagem indicando que o aluno não foi criado e a descrição do erro
            return Response({"Não foi criado o aluno!": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        