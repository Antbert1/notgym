from rest_framework import serializers
from .models import Category, Classdetail
from drf_writable_nested import WritableNestedModelSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ClassdetailSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Classdetail
        fields = ["name", "type", "tags", "blurb", "lat", "lng", "categories", "user"]
