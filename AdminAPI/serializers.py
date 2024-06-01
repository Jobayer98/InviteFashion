from rest_framework import serializers

from InviteFashionAPI.models import Product, ProductItem, Variant, Category, SubCategory, Brand, Color, Size

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
        
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

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
         
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'
        
class VariantSerializer(serializers.ModelSerializer):
    color = serializers.StringRelatedField(read_only=True)
    size = serializers.StringRelatedField(read_only=True)
    color_id = serializers.IntegerField(write_only=True)
    size_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Variant
        fields ='__all__'
        
class ProductItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    variants = VariantSerializer(read_only=True, many=True)
    product_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = ProductItem
        fields = ['id','product', 'original_price', 'sale_price', 'image_url', 'product_id', 'variants']