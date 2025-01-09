
# **Recipe Management API**

This is a RESTful API for managing recipes, built using **Django** and **Django REST Framework**. It allows users to create, view, update, delete, and search recipes. The API uses **JWT (JSON Web Token)** authentication to secure endpoints.

---

## **Features**

- **User Authentication** using JWT.
- **CRUD operations** for managing recipes:
  - Create a new recipe.
  - Retrieve a list of recipes or a single recipe.
  - Update or delete recipes (only allowed for the creator of the recipe).
- **Recipe Search**:
  - Search recipes by title, description, ingredients, or category.
- **Secure access**:
  - Only authenticated users can create or modify recipes.
  - Users can only update or delete recipes they created.

---

## **Technologies Used**

- **Django** - Web framework.
- **Django REST Framework** - Toolkit for building Web APIs.
- **Django REST Framework Simple JWT** - Authentication library using JWT.
- **SQLite** - Default database (can be switched to PostgreSQL or MySQL).
- **Postman** - For API testing.

---

## **Installation**

Follow these steps to set up and run the project locally:

### **1. Clone the repository**

```bash
git clone <your-repository-url>
cd recipe-management-api
```

### **2. Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

### **4. Apply migrations**

```bash
python manage.py migrate
```

### **5. Create a superuser**

```bash
python manage.py createsuperuser
```

Follow the prompts to set up an admin account.

### **6. Run the server**

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

---

## **API Endpoints**

| Method | Endpoint              | Description                              | Authentication |
|--------|-----------------------|------------------------------------------|----------------|
| POST   | `/api/token/`         | Obtain JWT access and refresh tokens     | No             |
| POST   | `/api/token/refresh/` | Refresh the access token                 | No             |
| GET    | `/recipes/`           | List all recipes                         | Yes            |
| POST   | `/recipes/`           | Create a new recipe                      | Yes            |
| GET    | `/recipes/<id>/`      | Retrieve a specific recipe by ID         | Yes            |
| PUT    | `/recipes/<id>/`      | Update a specific recipe by ID           | Yes (Creator)  |
| DELETE | `/recipes/<id>/`      | Delete a specific recipe by ID           | Yes (Creator)  |
| GET    | `/recipes/search/`    | Search recipes by query                  | No             |

---

## **Authentication**

This API uses **JWT (JSON Web Token)** for authentication. To access protected endpoints, you need to include a valid JWT token in the `Authorization` header of your requests.

### **Steps to get a token:**

1. Make a `POST` request to `/api/token/` with the following payload:
   ```json
   {
     "username": "your_username",
     "password": "your_password"
   }
   ```

2. The response will contain the access and refresh tokens:
   ```json
   {
     "access": "<access_token>",
     "refresh": "<refresh_token>"
   }
   ```

3. Include the access token in the `Authorization` header for protected endpoints:
   ```bash
   Authorization: Bearer <access_token>
   ```

---

## **Usage**

You can test the API using **Postman** or **cURL**:

### **Example Request: Create a Recipe**

**Endpoint**: `POST /recipes/`

**Headers**:
```bash
Authorization: Bearer <your_access_token>
Content-Type: application/json
```

**Payload**:
```json
{
  "title": "Spaghetti Carbonara",
  "description": "A classic Italian pasta dish with eggs, cheese, pancetta, and pepper.",
  "ingredients": "Spaghetti, Eggs, Pancetta, Parmesan Cheese, Black Pepper",
  "category": "Italian"
}
```

**Response**:
```json
{
  "id": 1,
  "user": 1,
  "title": "Spaghetti Carbonara",
  "description": "A classic Italian pasta dish with eggs, cheese, pancetta, and pepper.",
  "ingredients": "Spaghetti, Eggs, Pancetta, Parmesan Cheese, Black Pepper",
  "category": "Italian",
  "created_at": "2025-01-09T12:34:56Z"
}
```

---

## **Project Structure**

```bash
recipe-management-api/
├── manage.py
├── myapp/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── requirements.txt
└── ...
```

---

## **Future Enhancements**

- Add user registration and password reset endpoints.
- Implement pagination for listing recipes.
- Enable image uploads for recipes.
- Add unit tests for better code coverage.

---

## **License**

This project is licensed under the Alx BE License.

