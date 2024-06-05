from rest_framework import serializers

from InviteFashionAPI.models import Product, Category, SubCategory, Brand, Size

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
        fields = '__all__'
        # fields = ['id', 'title', 'description', 'category', 'sub_category', 'brand', 'category_id', 'sub_category_id', 'brand_id']
         
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'
        