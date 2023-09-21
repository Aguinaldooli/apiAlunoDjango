from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import AlunoModel
from api.serializers.alunoSerializer import AlunoSerializer

class AlunoUpdate(APIView):
    def put(self, request, id):
        try:
            aluno = AlunoModel.objects.get(pk=id)
            serializer = AlunoSerializer(aluno, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AlunoModel.DoesNotExist:
            return Response({"Aluno não encontrado"}, status=status.HTTP_404_NOT_FOUND)