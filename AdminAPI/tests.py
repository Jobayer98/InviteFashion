from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from InviteFashionAPI.models import (Brand, Category, SubCategory, Product, Size)
from .serializers import (BrandSerializer, CategorySerializer, SubCategorySerializer, ProductSerializer, SizeSerializer)

# Test case for Brand View
class BrandViewTests(APITestCase):
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        self.brand1 = Brand.objects.create(title='Brand1')
        self.brand2 = Brand.objects.create(title='Brand2')
        
    def test_list_brands(self):
        self.client.login(username='admin', password='password')
        url = reverse('brand-list')
        response = self.client.get(url)
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_create_brand(self):
        self.client.login(username='admin', password='password')
        url = reverse('brand-list')
        data = {'title': 'Brand3'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Brand.objects.count(), 3)
        self.assertEqual(Brand.objects.get(id=response.data['id']).title, 'Brand3')

class BrandDetailViewTests(APITestCase):
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        self.brand = Brand.objects.create(title='Brand1')
        
    def test_retrieve_brand(self):
        self.client.login(username='admin', password='password')
        url = reverse('brand-detail', kwargs={'pk': self.brand.pk})
        response = self.client.get(url)
        serializer = BrandSerializer(self.brand)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_update_brand(self):
        self.client.login(username='admin', password='password')
        url = reverse('brand-detail', kwargs={'pk': self.brand.pk})
        data = {'title': 'UpdatedBrand'}
        response = self.client.put(url, data, format='json')
        self.brand.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.brand.title, 'UpdatedBrand')
    
    def test_delete_brand(self):
        self.client.login(username='admin', password='password')
        url = reverse('brand-detail', kwargs={'pk': self.brand.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Brand.objects.count(), 0)

# Test case for Category View
class CategoryViewTests(APITestCase):
    
    def setUp(self):
        # Create a user and a few categories for testing
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        self.category1 = Category.objects.create(title='Category1')
        self.category2 = Category.objects.create(title='Category2')
        
    def test_list_categories(self):
        self.client.login(username='admin', password='password')
        url = reverse('category-list')
        response = self.client.get(url)
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_create_category(self):
        self.client.login(username='admin', password='password')
        url = reverse('category-list')
        data = {'title': 'Category3'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 3)
        self.assertEqual(Category.objects.get(id=response.data['id']).title, 'Category3')

class CategoryDetailViewTests(APITestCase):
    
    def setUp(self):
        # Create a user and a few categories for testing
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        self.category = Category.objects.create(title='Category1')
        
    def test_retrieve_category(self):
        self.client.login(username='admin', password='password')
        url = reverse('category-detail', kwargs={'pk': self.category.pk})
        response = self.client.get(url)
        serializer = CategorySerializer(self.category)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_update_category(self):
        self.client.login(username='admin', password='password')
        url = reverse('category-detail', kwargs={'pk': self.category.pk})
        data = {'title': 'UpdatedCategory'}
        response = self.client.put(url, data, format='json')
        self.category.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.category.title, 'UpdatedCategory')
    
    def test_delete_category(self):
        self.client.login(username='admin', password='password')
        url = reverse('category-detail', kwargs={'pk': self.category.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

# Test case for Subcategory view
class SubCategoryListViewTests(APITestCase):
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        self.subcategory1 = SubCategory.objects.create(title='SubCategory1')
        self.subcategory2 = SubCategory.objects.create(title='SubCategory2')
        
    def test_list_subcategories(self):
        url = reverse('subcategory-list')
        response = self.client.get(url)
        subcategories = SubCategory.objects.all()
        serializer = SubCategorySerializer(subcategories, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_create_subcategory(self):
        self.client.login(username='admin', password='password')
        url = reverse('subcategory-list')
        data = {'title': 'SubCategory3'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SubCategory.objects.count(), 3)
        self.assertEqual(SubCategory.objects.get(id=response.data['id']).title, 'SubCategory3')

class SubCategoryDetailViewTests(APITestCase):
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        self.subcategory = SubCategory.objects.create(title='SubCategory1')
        
    def test_retrieve_subcategory(self):
        self.client.login(username='admin', password='password')
        url = reverse('subcategory-detail', kwargs={'pk': self.subcategory.pk})
        response = self.client.get(url)
        serializer = SubCategorySerializer(self.subcategory)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_update_subcategory(self):
        self.client.login(username='admin', password='password')
        url = reverse('subcategory-detail', kwargs={'pk': self.subcategory.pk})
        data = {'title': 'UpdatedSubCategory'}
        response = self.client.put(url, data, format='json')
        self.subcategory.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.subcategory.title, 'UpdatedSubCategory')
    
    def test_delete_subcategory(self):
        self.client.login(username='admin', password='password')
        url = reverse('subcategory-detail', kwargs={'pk': self.subcategory.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SubCategory.objects.count(), 0)
        
# Test case for product view
class ProductListViewTests(APITestCase):
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        self.category = Category.objects.create(title='Category1')
        self.sub_category = SubCategory.objects.create(title='SubCategory1')
        self.brand = Brand.objects.create(title='Brand1')
        
        self.product1 = Product.objects.create(
            title='Product1',
            description='Description1',
            category=self.category,
            sub_category=self.sub_category,
            brand=self.brand
        )
        self.product2 = Product.objects.create(
            title='Product2',
            description='Description2',
            category=self.category,
            sub_category=self.sub_category,
            brand=self.brand
        )
        
    def test_list_products(self):
        self.client.login(username='admin', password='password')
        url = reverse('product-list')
        response = self.client.get(url)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_create_product(self):
        self.client.login(username='admin', password='password')
        url = reverse('product-list')
        data = {
            'title': 'Product3',
            'description': 'Description3',
            'category_id': self.category.id,
            'sub_category_id': self.sub_category.id,
            'brand_id': self.brand.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 3)
        self.assertEqual(Product.objects.get(id=response.data['id']).title, 'Product3')

class ProductDetailViewTests(APITestCase):
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        self.category = Category.objects.create(title='Category1')
        self.sub_category = SubCategory.objects.create(title='SubCategory1')
        self.brand = Brand.objects.create(title='Brand1')
        self.product = Product.objects.create(
            title='Product1',
            description='Description1',
            category=self.category,
            sub_category=self.sub_category,
            brand=self.brand
        )
        
    def test_retrieve_product(self):
        self.client.login(username='admin', password='password')
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        response = self.client.get(url)
        serializer = ProductSerializer(self.product)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_update_product(self):
        self.client.login(username='admin', password='password')
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        data = {
            'title': 'UpdatedProduct',
            'description': 'UpdatedDescription',
            'category_id': self.category.id,
            'sub_category_id': self.sub_category.id,
            'brand_id': self.brand.id
        }
        response = self.client.put(url, data, format='json')
        self.product.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.product.title, 'UpdatedProduct')
        self.assertEqual(self.product.description, 'UpdatedDescription')
    
    def test_delete_product(self):
        self.client.login(username='admin', password='password')
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
        
