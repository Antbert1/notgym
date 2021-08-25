from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("users", views.UserViewset)
router.register("classdetails", views.ClassdetailViewset)
router.register("categories", views.CategoryViewset)

urlpatterns = [
    path("", include(router.urls)),
]
