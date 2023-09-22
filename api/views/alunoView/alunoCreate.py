from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import AlunoModel
from api.serializers.alunoSerializer import AlunoSerializer

class AlunoCreate(APIView):
    def post(self, request):
        serializer = AlunoSerializer(data=request.data)
        # Verifica se os dados fornecidos são válidos de acordo com o serializador          
        if serializer.is_valid():
            # Se for válido ele vai salvar e retornar uma menssagem com êxito
            serializer.save()
            message = "Aluno criado com êxito."
            return Response({"message": message, "data": serializer.data}, status=status.HTTP_201_CREATED)
        # Caso não seja válido os dados do body ele retorna o erro específico
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)