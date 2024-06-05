from django.urls import path

from . import views

urlpatterns = [
    path('category', views.CategoryView.as_view(), name='category-list'),
    path('subcategory', views.SubCategoryView.as_view(), name='subcategory-list'),
    path('brand', views.BrandView.as_view(), name='brand-list'),
    path('products', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
]