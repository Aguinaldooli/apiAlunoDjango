from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import AlunoModel
from api.serializers.alunoSerializer import AlunoSerializer

class AlunoCreate(APIView):
    def post(self, request):
        serializer = AlunoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)