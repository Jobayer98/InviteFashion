from rest_framework import serializers

from .models import Product, ProductItem, Variant, Category, SubCategory, Brand

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['name']
        
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    sub_category = serializers.StringRelatedField(read_only=True)
    brand = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    sub_category_id = serializers.IntegerField(write_only=True)
    brand_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'category', 'sub_category', 'brand', 'category_id', 'sub_category_id', 'brand_id']
        
        