from rest_framework.serializers import ModelSerializer
from .models import Book


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'