from rest_framework import serializers
from .models import Products, Category, Store


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields  = ['name', 'description', 'quantity', 'category', 'store']



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields  = ['name', 'description', 'slug']

class StoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields  = ['name', 'type', 'state', 'country', 'totalCapacity', 'contactPhone', 'contactEmail', 'storeHeadId']
      
        








