from rest_framework import generics, permissions


from InviteFashionAPI.models import Product, ProductItem, Variant, Category, SubCategory, Brand, Size, Color
from InviteFashionAPI.serializers import ProductSerializer, CategorySerializer, SubCategorySerializer, BrandSerializer


class BrandView(generics.ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [permissions.IsAdminUser]
    
class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [permissions.IsAdminUser]

