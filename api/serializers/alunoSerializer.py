from rest_framework import serializers
from api.models import AlunoModel

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlunoModel
        fields = '__all__'