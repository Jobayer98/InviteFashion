from django.urls import path

from . import views

urlpatterns = [
    path('brands', views.BrandView.as_view(), name='brand-list'),
    path('brands/<int:pk>', views.BrandDetailView.as_view(), name='brand-detail'),
    path('colors', views.ColorListView.as_view(), name='color-list'),
    path('colors/<int:pk>', views.ColorDetailView.as_view(), name='color-detail'),
    path('sizes', views.SizeListView.as_view(), name='size-list'),
    path('sizes/<int:pk>', views.SizeDetailView.as_view(), name='size-detail'),
    path('categories', views.CategoryView.as_view(), name='category-list'),
    path('categories/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('sub-categories', views.SubCategoryListView.as_view(), name='subcategory-list'),
    path('sub-categories/<int:pk>', views.SubCategoryDetailView.as_view(), name='subcategory-detail'),
    path('products', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('product-items', views.ProductItemListView.as_view(), name='product-items-list'),
    path('product-items/<int:pk>', views.ProductItemDetailView.as_view(), name='product-item-detail'),
    path('variants', views.VariantListView.as_view(), name='variant-list'),
    path('variants/<int:pk>', views.VariantDetailView.as_view(), name='variant-detail'),
   
]