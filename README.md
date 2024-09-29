#  Fashion E-Commerce API

## Description:
The Fashion E-Commerce API provides a backend solution for managing a fashion e-commerce platform, offering distinct privileges for users and admins.
This API is designed to streamline e-commerce operations for both users and admins, providing a robust set of endpoints for product management, order processing, and customer interactions.

- **Admin Privileges:**
  - Manage products (CRUD operations: create, read, update, delete).
  - Manage users (create, update, delete).
  - Manage orders (view, update status).
  - Manage product categories, and inventory.

- **User Privileges:**
  - Browse products.
  - View product details.
  - Add items to cart.
  - Make purchases and create orders.
  - Manage their account and profile (update details, change password).

## Technologies Used:
- **Backend Framework:** Django REST Framework (DRF)
- **Database:** SQL (SQLite)
- **Authentication:** JWT (JSON Web Token) for secure user authentication and session management.
- **Environment Management:** Python 3.x and virtualenv.

## Installation Steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Jobayer98/InviteFashion.git
    ```

2. **Navigate into the project directory:**
    ```bash
    cd InviteFashion
    ```

3. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\\Scripts\\activate
    ```

4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the database:**
    - Configure your database settings in `settings.py` file under the `DATABASES` section.
    - Run the following command to apply migrations and create necessary tables:
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser (Admin account):**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

8. **Access the API:**
    - Visit `http://127.0.0.1:8000/api/v1/` to access the API endpoints.
    - Visit `http://127.0.0.1:8000/api/v1/admin` to access the Admin API endpoints.
    - Visit `http://127.0.0.1:8000/admin/` to access the Django admin panel.

## API Endpoints:

### **Authentication**
1. **Register User**  
   - **Endpoint:** `/api/v1/auth/register/`  
   - **Method:** `POST`  
   - **Request Body:**  
     ```json
     {
       "username": "string",
       "email": "string",
       "password": "string"
     }
     ```

2. **Login User**  
   - **Endpoint:** `/api/v1/auth/login/`  
   - **Method:** `POST`  
   - **Request Body:**  
     ```json
     {
       "username": "string",
       "password": "string"
     }
     ```

### **Products**
1. **Get All Products**  
   - **Endpoint:** `/api/v1/products/`  
   - **Method:** `GET`  
   - **Query Params:**  
     - `category`: Filter by product category  
     - `price_min`: Minimum price  
     - `price_max`: Maximum price  

2. **Get Product Details**  
   - **Endpoint:** `/api/v1/products/{id}/`  
   - **Method:** `GET`  
   - **Path Params:**  
     - `id`: ID of the product  

3. **Create Product (Admin)**  
   - **Endpoint:** `/api/v1/products/`  
   - **Method:** `POST`  
   - **Request Body:**  
     ```json
     {
       "name": "string",
       "description": "string",
       "price": "number",
       "stock": "number",
       "category": "string"
     }
     ```

4. **Update Product (Admin)**  
   - **Endpoint:** `/api/v1/products/{id}/`  
   - **Method:** `PUT`  
   - **Request Body:**  
     ```json
     {
       "name": "string",
       "description": "string",
       "price": "number",
       "stock": "number",
       "category": "string"
     }
     ```

5. **Delete Product (Admin)**  
   - **Endpoint:** `/api/v1/products/{id}/`  
   - **Method:** `DELETE`  
   - **Path Params:**  
     - `id`: ID of the product

### **Cart**
1. **View Cart (User)**  
   - **Endpoint:** `/api/v1/cart/`  
   - **Method:** `GET`  

2. **Add to Cart (User)**  
   - **Endpoint:** `/api/v1/cart/`  
   - **Method:** `POST`  
   - **Request Body:**  
     ```json
     {
       "product_id": "integer",
       "quantity": "integer"
     }
     ```

3. **Update Cart Item (User)**  
   - **Endpoint:** `/api/v1/cart/{id}/`  
   - **Method:** `PUT`  
   - **Request Body:**  
     ```json
     {
       "quantity": "integer"
     }
     ```

4. **Delete Cart Item (User)**  
   - **Endpoint:** `/api/v1/cart/{id}/`  
   - **Method:** `DELETE`  

### **Orders**
1. **Create Order (User)**  
   - **Endpoint:** `/api/v1/orders/`  
   - **Method:** `POST`  
   - **Request Body:**  
     ```json
     {
       "shipping_address": "string",
       "payment_method": "string"
     }
     ```

2. **View Order Details (User/Admin)**  
   - **Endpoint:** `/api/v1/orders/{id}/`  
   - **Method:** `GET`  

3. **Update Order Status (Admin)**  
   - **Endpoint:** `/api/v1/orders/{id}/`  
   - **Method:** `PUT`  
   - **Request Body:**  
     ```json
     {
       "status": "string"
     }
     ```

### **Categories (Admin)**
1. **List Categories**  
   - **Endpoint:** `/api/v1/categories/`  
   - **Method:** `GET`  

2. **Create Category (Admin)**  
   - **Endpoint:** `/api/v1/categories/`  
   - **Method:** `POST`  
   - **Request Body:**  
     ```json
     {
       "name": "string"
     }
     ```

3. **Update Category (Admin)**  
   - **Endpoint:** `/api/v1/categories/{id}/`  
   - **Method:** `PUT`  
   - **Request Body:**  
     ```json
     {
       "name": "string"
     }
     ```

4. **Delete Category (Admin)**  
   - **Endpoint:** `/api/v1/categories/{id}/`  
   - **Method:** `DELETE`  

