# 🧾 Inventory API

A RESTful Inventory Management API built with Django and Django REST Framework. It consists of two modular apps:

- *User App*: Manages user accounts with full CRUD operations.
- *Product App*: Manages products associated with users, including category-based filtering.

---

## 🚀 Features

### User App
- Create a new user
- Retrieve user details
- Update user information
- Delete a user

### Product App
- Add new products
- Retrieve product details
- Update product information
- Delete products
- Filter products by category

---

## 🛠️ Tech Stack

- Python 3.11+
- Django 4.x
- Django REST Framework
- SQLite (default) or PostgreSQL
- Postman (for API testing)

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/inventory-api.git
cd inventory-api
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver