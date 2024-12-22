from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models

# To customization of users and superusers.
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

# Collection == Group
class Collection(models.Model):
    name = models.CharField(max_length=100, unique=True)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def add_points(self, points):
        self.points += points
        self.save()

    def deduct_points(self, points):
        if points > self.points:
            raise ValueError("Not enough points in the collection.")
        self.points -= points
        self.save()

#Extens Django built-in user.
class Customer(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    individual_points = models.PositiveIntegerField(default=0)
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, blank=True, related_name="members")

    objects = CustomerManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    def add_points(self, points):
        self.individual_points += points
        self.save()
        if self.collection:
            self.collection.add_points(points)

    def deduct_points(self, points):
        if points > self.individual_points:
            raise ValueError("Not enough points in the individual account.")
        self.individual_points -= points
        self.save()
        if self.collection:
            self.collection.deduct_points(points)

    def redeem_points(self, points):
        if points > self.individual_points:
            raise ValueError("Not enough points to redeem.")
        self.deduct_points(points)
        return points / 100.0


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="purchases")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    points_earned = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    # This is responsible for awarding points to the customer when a purchase is made.
    def save(self, *args, **kwargs):
        if not self.pk:
            self.customer.add_points(self.points_earned)
        super().save(*args, **kwargs)
