from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser


ROLE_USER = 'USER'
ROLE_ADMIN = 'ADMIN'
ROLE_STOREKEEPER = 'STOREKEEPER'

ASSET = 'ASSET'
FOR_SALE = 'FOR SALE'

PRODUCT_TYPES = [
    (ASSET, 'Asset'),
    (FOR_SALE, 'for sale'),
]

ROLE_CHOICES = [
    (ROLE_USER, 'User'),
    (ROLE_ADMIN, 'Admin'),
    (ROLE_STOREKEEPER, 'Storekeeper'),
]


class User(AbstractUser):
    """Custom user model that extends Django's AbstractUser and adds a role."""
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_USER)


    

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children', on_delete=models.CASCADE
    )
    # optional if categories are per-store; remove if categories are global
    store_id = models.UUIDField(null=True, blank=True, db_index=True)

    is_active = models.BooleanField(default=True)
    metadata = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        unique_together = (('slug', 'store_id'),)
        indexes = [
            models.Index(fields=['store_id', 'slug']),
        ]

    def __str__(self):
        return self.name
    
class Store(models.Model):
      id = models.UUIDField(primary_key=True, default=uuid4, editable=False)      
      name  = models.CharField(max_length=50)
      type = models.CharField(max_length=50)
      addressLine = models.CharField(max_length=50)
      city = models.CharField(max_length=50)
      state = models.CharField(max_length=50)
      country = models.CharField(max_length=50)
      totalCapacity = models.CharField(max_length=50)
      contactPhone = models.CharField(max_length=50)
      contactEmail = models.EmailField(max_length=254)
      isActive = models.BooleanField(default = False)
      storeHeadId = models.ForeignKey(User, on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      def __str__(self):
        return self.name




class Products(models.Model):
    is_active = models.BooleanField(default=False)
    id  = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=50)
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    product_type = models.CharField(choices=PRODUCT_TYPES, max_length=50)
    description = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    

    

    

