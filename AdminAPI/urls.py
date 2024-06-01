from django.urls import path

from . import views

urlpatterns = [
    path('brands', views.BrandView.as_view(), name='brand-list'),
    path('brands/<int:pk>', views.BrandDetailView.as_view(), name='category-detail'),
    path('categories', views.CategoryView.as_view(), name='category-list'),
    path('categories/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    # path('products', views.ProductListView.as_view(), name='product-list'),
    # path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
   
]