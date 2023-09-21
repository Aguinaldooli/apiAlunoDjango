from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import AlunoModel
from api.serializers.alunoSerializer import AlunoSerializer

class AlunoList(APIView):
    def get(self, request):
        try:
            alunos = AlunoModel.objects.all()
            serializer = AlunoSerializer(alunos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Não foi criado o aluno!": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        