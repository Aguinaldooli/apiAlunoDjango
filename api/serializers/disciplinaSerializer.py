from rest_framework import serializers
from api.models import DisciplinaModel

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplinaModel
        fields = '__all__'