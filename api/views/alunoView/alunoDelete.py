from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from api.models import AlunoModel
from api.serializers.alunoSerializer import AlunoSerializer

class AlunoDelete(generics.DestroyAPIView):
    queryset = AlunoModel.objects.all()
    serializer_class = AlunoSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response({"message": "Aluno excluído com sucesso."}, status=status.HTTP_204_NO_CONTENT)
        except AlunoModel.DoesNotExist:
            return Response({"message": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": "Erro ao excluir o aluno: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)