from notgym.models import Classdetail
from django.contrib import admin
from .models import Category, Classdetail, UserProfile

admin.site.register(Classdetail)
admin.site.register(Category)
admin.site.register(UserProfile)
