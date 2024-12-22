from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomerManager(BaseUserManager):
    def _create_customer(self, username, password=None, **extra_fields):
        customer = self.model(username=username, **extra_fields)
        customer.set_password(password)
        customer.save(using=self._db)
        return customer

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_customer(username, password, **extra_fields)

class Customer(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    individual_points = models.PositiveIntegerField(default=0)

    objects = CustomerManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    def add_points(self, purchase_amount):
        points_earned = int(purchase_amount * 10)
        self.individual_points += points_earned
        self.save()

    def redeem_points(self, points_to_redeem):
        discount = points_to_redeem / 100
        self.individual_points -= points_to_redeem

        self.save()
        return discount