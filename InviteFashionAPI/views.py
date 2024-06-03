from rest_framework import generics

from .models import Category, SubCategory, Brand, ProductItem
from .serializers import CategorySerializer, SubCategorySerializer, BrandSerializer, ProductItemSerializer, ProductItemDetailSerializer

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class SubCategoryView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    
class BrandView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
        
class ProductListView(generics.ListAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    
class ProductDetailView(generics.ListAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemDetailSerializer