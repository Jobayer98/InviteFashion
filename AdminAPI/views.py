from rest_framework import generics, permissions

from InviteFashionAPI.models import Product, Category, SubCategory, Brand, Size
from .serializers import BrandSerializer, CategorySerializer, SubCategorySerializer, ProductSerializer, SizeSerializer


class BrandView(generics.ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [permissions.IsAdminUser]
    
class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [permissions.IsAdminUser]


class CategoryView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser]
    
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser]
    
class SubCategoryListView(generics.ListCreateAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    
class SubCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    permission_classes = [permissions.IsAdminUser]
    
class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]
    
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]
    
class SizeListView(generics.ListCreateAPIView):
    serializer_class = SizeSerializer
    queryset = Size.objects.all()
    permission_classes = [permissions.IsAdminUser]
    
class SizeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SizeSerializer
    queryset = Size.objects.all()
    permission_classes = [permissions.IsAdminUser]
