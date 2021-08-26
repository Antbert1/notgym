from notgym.serializers import ClassdetailSerializer, CategorySerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from .models import Classdetail, Category, UserProfile
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "email")


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ClassdetailViewset(viewsets.ModelViewSet):
    serializer_class = ClassdetailSerializer
    queryset = Classdetail.objects.all()

    # Token stuff, may not need
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        """
        #checks if post request data is an array initializes serializer with many=True
        else executes default CreateModelMixin.create function
        """
        # currentDate = datetime.date.today()
        # data = request.data
        is_many = isinstance(request.data, list)
        if not is_many:
            return super(ClassdetailViewset, self).create(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            return Response(
                request.data, status=status.HTTP_201_CREATED, headers=headers
            )


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
