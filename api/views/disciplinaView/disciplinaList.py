from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models.disciplinaModel import DisciplinaModel  
from api.serializers.disciplinaSerializer import DisciplinaSerializer  

class DisciplinaList(APIView):
    def get(self, request):
        try:
            disciplinas = DisciplinaModel.objects.all()
            serializer = DisciplinaSerializer(disciplinas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Erro ao listar disciplinas": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)