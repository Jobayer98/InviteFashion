from rest_framework import generics
from rest_framework.response import Response

from .models import Category, SubCategory, Brand, Product
from .serializers import CategorySerializer, SubCategorySerializer, BrandSerializer, ProductSerializer

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
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer()
    
    def list(self, request):
        products = self.get_queryset()
        category_name = request.query_params.get('category')
        subcategory_name = request.query_params.get('subcategory')
        brand_name = request.query_params.get('brand')
        
        if category_name:
            products = products.filter(category__name=category_name)
        if subcategory_name:
            products = products.filter(sub_category__name=subcategory_name)
        if brand_name:
            products = products.filter(brand__name=brand_name)
            
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
             