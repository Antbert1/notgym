from notgym.serializers import ClassdetailSerializer, CategorySerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Classdetail, Category
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ClassdetailViewset(viewsets.ModelViewSet):
    serializer_class = ClassdetailSerializer
    queryset = Classdetail.objects.all()

    # Token stuff, may not need
    # authentication_classes = (TokenAuthentication,)
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
