from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Classdetail, UserProfile
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "email",
            "name",
            "password",
            "is_teacher",
            "first_name",
            "last_name",
            "postcode",
        )
        extra_kwargs = {
            "password": {
                "write_only": True,
                "required": True,
                "style": {"input_type": "password"},
            }
        }

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     Token.objects.create(user=user)
    #     return user

    def update(self, instance, validated_data):
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)

        return super().update(instance, validated_data)

    def create(self, validated_data):
        # user = UserProfile.objects.create_user(
        #     email=validated_data["email"],
        #     name=validated_data["name"],
        #     is_teacher=validated_data["is_teacher"],
        #     first_name=validated_data["first_name"],
        #     last_name=validated_data["last_name"],
        #     postcode=validated_data["postcode"],
        #     password=validated_data["password"],
        # )
        user = UserProfile.objects.create_user(**validated_data)
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
