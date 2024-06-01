from django.contrib import admin

from .models import Brand, Category, Product, SubCategory, Size, Color, ProductItem, Review, Variant

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ProductItem)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Review)
admin.site.register(Variant)
