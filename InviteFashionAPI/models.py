from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
class ProductItem(models.Model):
    original_price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_code = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.URLField(max_length=100)
    porduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.porduct.title} | {self.product_code}"
    
class Review(models.Model):
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, blank=True, null=True)
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
            return f"{self.pk} | {self.menu_item.title} | {self.rating}"
        
class Size(models.Model):
    size = models.CharField(max_length=5)
    
    def __str__(self) -> str:
        return self.size
    
class Color(models.Model):
    color = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.color
    
class Variant(models.Model):
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    quantity_in_stock = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return f"{self.product_item.pk} | {self.size} | {self.color}"