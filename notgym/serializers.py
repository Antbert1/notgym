from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Classdetail
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {
            "password": {
                "write_only": True,
                "required": True,
                "style": {"input_type": "password"},
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ClassdetailSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Classdetail
        fields = ["name", "type", "tags", "blurb", "lat", "lng", "categories", "user"]
