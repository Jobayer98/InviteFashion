from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category
    
class SubCategory(models.Model):
    subcategory = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subcategory
    
class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.brand_name
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    original_price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_code = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.URLField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
        
class Size(models.Model):
    size = models.CharField(max_length=10)
    quantity_in_stock = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.size
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, blank=True, null=True)
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
            return f"{self.pk} | {self.rating}"