from django.contrib import admin

from .models import Brand, Category, Product, SubCategory, Size, Review

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Review)
