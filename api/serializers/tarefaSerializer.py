from rest_framework import serializers
from api.models import TarefaModel

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarefaModel
        fields = '__all__'

class TarefaPartialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarefaModel
        fields = ['titulo', 'descricao', 'data_entrega', 'concluida']