from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from InviteFashionAPI.models import Brand, Category, SubCategory, Product, ProductItem, Variant, Color, Size
from .serializers import BrandSerializer, CategorySerializer, SubCategorySerializer, ProductSerializer, ProductItemSerializer, VariantSerializer, ColorSerializer, SizeSerializer

# Test case for Brand View
class BrandViewTests(APITestCase):
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        self.brand1 = Brand.objects.create(name='Brand1')
        self.brand2 = Brand.objects.create(name='Brand2')
        
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
        data = {'name': 'Brand3'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Brand.objects.count(), 3)
        self.assertEqual(Brand.objects.get(id=response.data['id']).name, 'Brand3')

class BrandDetailViewTests(APITestCase):
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        self.brand = Brand.objects.create(name='Brand1')
        
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
        data = {'name': 'UpdatedBrand'}
        response = self.client.put(url, data, format='json')
        self.brand.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.brand.name, 'UpdatedBrand')
    
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
        self.category1 = Category.objects.create(name='Category1')
        self.category2 = Category.objects.create(name='Category2')
        
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
        data = {'name': 'Category3'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 3)
        self.assertEqual(Category.objects.get(id=response.data['id']).name, 'Category3')

class CategoryDetailViewTests(APITestCase):
    
    def setUp(self):
        # Create a user and a few categories for testing
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        self.category = Category.objects.create(name='Category1')
        
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
        data = {'name': 'UpdatedCategory'}
        response = self.client.put(url, data, format='json')
        self.category.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.category.name, 'UpdatedCategory')
    
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
        self.subcategory1 = SubCategory.objects.create(name='SubCategory1')
        self.subcategory2 = SubCategory.objects.create(name='SubCategory2')
        
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
        data = {'name': 'SubCategory3'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SubCategory.objects.count(), 3)
        self.assertEqual(SubCategory.objects.get(id=response.data['id']).name, 'SubCategory3')


class SubCategoryDetailViewTests(APITestCase):
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        self.subcategory = SubCategory.objects.create(name='SubCategory1')
        
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
        data = {'name': 'UpdatedSubCategory'}
        response = self.client.put(url, data, format='json')
        self.subcategory.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.subcategory.name, 'UpdatedSubCategory')
    
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
        self.category = Category.objects.create(name='Category1')
        self.sub_category = SubCategory.objects.create(name='SubCategory1')
        self.brand = Brand.objects.create(name='Brand1')
        
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
        self.category = Category.objects.create(name='Category1')
        self.sub_category = SubCategory.objects.create(name='SubCategory1')
        self.brand = Brand.objects.create(name='Brand1')
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
        


class ColorListViewTests(APITestCase):
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        self.color1 = Color.objects.create(name='Color1')
        self.color2 = Color.objects.create(name='Color2')
        
    def test_list_colors(self):
        self.client.login(username='admin', password='password')
        url = reverse('color-list')
        response = self.client.get(url)
        colors = Color.objects.all()
        serializer = ColorSerializer(colors, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_create_color(self):
        self.client.login(username='admin', password='password')
        url = reverse('color-list')
        data = {'name': 'Color3'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Color.objects.count(), 3)
        self.assertEqual(Color.objects.get(id=response.data['id']).name, 'Color3')

class ColorDetailViewTests(APITestCase):
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        self.color = Color.objects.create(name='Color1')
        
    def test_retrieve_color(self):
        self.client.login(username='admin', password='password')
        url = reverse('color-detail', kwargs={'pk': self.color.pk})
        response = self.client.get(url)
        serializer = ColorSerializer(self.color)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_update_color(self):
        self.client.login(username='admin', password='password')
        url = reverse('color-detail', kwargs={'pk': self.color.pk})
        data = {'name': 'UpdatedColor'}
        response = self.client.put(url, data, format='json')
        self.color.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.color.name, 'UpdatedColor')
    
    def test_delete_color(self):
        self.client.login(username='admin', password='password')
        url = reverse('color-detail', kwargs={'pk': self.color.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Color.objects.count(), 0)

class SizeListViewTests(APITestCase):
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        self.sizee1 = Size.objects.create(size='Size1')
        self.sizee2 = Size.objects.create(size='Size2')
        
    def test_list_sizes(self):
        self.client.login(username='admin', password='password')
        url = reverse('size-list')
        response = self.client.get(url)
        sizes = Size.objects.all()
        serializer = SizeSerializer(sizes, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_create_size(self):
        self.client.login(username='admin', password='password')
        url = reverse('size-list')
        data = {'size': 'Size3'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Size.objects.count(), 3)
        self.assertEqual(Size.objects.get(id=response.data['id']).size, 'Size3')

class SizeDetailViewTests(APITestCase):
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        self.sizee = Size.objects.create(size='Size1')
        
    def test_retrieve_size(self):
        self.client.login(username='admin', password='password')
        url = reverse('size-detail', kwargs={'pk': self.sizee.pk})
        response = self.client.get(url)
        serializer = SizeSerializer(self.sizee)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_update_size(self):
        self.client.login(username='admin', password='password')
        url = reverse('size-detail', kwargs={'pk': self.sizee.pk})
        data = {'size': 'usize'}
        response = self.client.put(url, data, format='json')
        self.sizee.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.sizee.size, 'usize')
    
    def test_delete_size(self):
        self.client.login(username='admin', password='password')
        url = reverse('size-detail', kwargs={'pk': self.sizee.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Size.objects.count(), 0)
