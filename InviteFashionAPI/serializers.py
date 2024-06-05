from rest_framework import serializers

from .models import Product, Category, SubCategory, Brand, Size

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
        
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    sub_category = serializers.StringRelatedField(read_only=True)
    brand = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'sub_category', 'brand', 'original_price', 'discount_price']
    
        
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        exclude = ['product'] 
        
class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    sub_category = serializers.StringRelatedField(read_only=True)
    brand = serializers.StringRelatedField(read_only=True)
    variants = SizeSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id','title', 'category', 'sub_category', 'brand', 'original_price', 'discount_price', 'image_url', 'product_code', 'variants']
        