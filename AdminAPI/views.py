from rest_framework import generics, permissions


from InviteFashionAPI.models import Product, ProductItem, Variant, Category, SubCategory, Brand, Size, Color
from .serializers import BrandSerializer, CategorySerializer, SubCategorySerializer


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
    
class SubCategoryView(generics.ListCreateAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    
class SubCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    permission_classes = [permissions.IsAdminUser]