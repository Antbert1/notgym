from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class UserProfileManager(BaseUserManager):
    def create_user(
        self, email, name, is_teacher, first_name, last_name, postcode, password=None
    ):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            is_teacher=is_teacher,
            first_name=first_name,
            last_name=last_name,
            postcode=postcode,
        )

        user.set_password(password)
        user.save(using=self._db)
        # Token.objects.create(user=user)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, False, "", "", "", password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    # Database model for users in the system
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        # Retrieve full name of user
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    # classdetails = models.ManyToManyField(Classdetail, related_name="classdetails")


class Classdetail(models.Model):
    name = models.CharField(max_length=60)
    categories = models.ManyToManyField(Category, related_name="classdetails")
    type = models.CharField(max_length=60, default="")
    tags = models.TextField(default="")
    blurb = models.TextField(default="")
    lat = models.DecimalField(max_digits=18, decimal_places=15, default=0.0)
    lng = models.DecimalField(max_digits=18, decimal_places=15, default=0.0)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
