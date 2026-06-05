#faz a conversão dos dados do meu banco e permite que compartilhe aq importar 
#todos modelos q eu quiser serializar

from rest_framework import serializers
from app.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'