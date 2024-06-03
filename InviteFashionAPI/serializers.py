from rest_framework import serializers

from .models import Product, ProductItem, Variant, Category, SubCategory, Color, Brand, Size

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
        fields = ['id', 'title', 'description', 'category', 'sub_category', 'brand']
class ProductTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title']
        
class ProductItemSerializer(serializers.ModelSerializer):
    product = ProductTitleSerializer(read_only=True)
    class Meta:
        model = ProductItem
        fields = ['id', 'product', 'original_price', 'sale_price', 'image_url']
        
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'   
        
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'   
        
class VariantSerializer(serializers.ModelSerializer):
    color = ColorSerializer(read_only=True)
    size = SizeSerializer(read_only=True)
    class Meta:
        model = Variant
        fields = ['id', 'size', 'color', 'quantity_in_stock']
        
class ProductItemDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    variants = VariantSerializer(read_only=True, many=True)
    class Meta:
        model = ProductItem
        fields = ['id', 'product', 'original_price', 'sale_price', 'image_url', 'variants']
        