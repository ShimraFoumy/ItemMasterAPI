
📦 Item Master API

A **Django REST Framework (DRF)** based backend API for managing inventory items.
This project was developed step-by-step as part of a backend learning plan (Day 1–6), covering CRUD operations, testing, pagination, filtering, sorting, and admin configuration.

---

## 🚀 Features

### ✅ Core Features (Day 1–4)

* Create, Read, Update, Delete (CRUD) items
* Django ORM–based database operations
* RESTful API using Django REST Framework
* Admin panel support
* Automatic timestamps (`created_at`, `updated_at`)
* Reorder level validation
* Item status management (ACTIVE / INACTIVE)

---

### ✅ API Enhancements (Day 5–6)

* Pagination for item list endpoint
* Sorting (ordering) support
* Filtering by multiple fields
* Unit tests for CRUD operations
* Validation & error handling tests
* Improved Django Admin UI with columns

---

## 🛠 Tech Stack

* **Python 3.11**
* **Django**
* **Django REST Framework**
* **SQLite** (development)
* **Postman** (API testing)

---

## 📁 Project Structure

```
ItemMasterAPI/
│
├── config/          # Project settings & URLs
├── items/           # Items app (models, views, serializers, tests)
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ShimraFoumy/ItemMasterAPI.git
cd ItemMasterAPI
```

---

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create superuser

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Run the server

```bash
python manage.py runserver
```

---

## 🔗 API Endpoints

Base URL:

```
http://127.0.0.1:8000/api/
```

| Method | Endpoint              | Description                         |
| ------ | --------------------- | ----------------------------------- |
| GET    | `/items/`             | List all items (pagination enabled) |
| POST   | `/items/`             | Create new item                     |
| GET    | `/items/{id}/`        | Retrieve item                       |
| PUT    | `/items/{id}/update/` | Update item                         |
| DELETE | `/items/{id}/delete/` | Delete item                         |

---

## 🔍 Pagination, Sorting & Filtering

### Pagination

```
/api/items/?page=2
```

### Sorting

```
/api/items/?ordering=name
/api/items/?ordering=-quantity
```

### Filtering

```
/api/items/?status=ACTIVE
/api/items/?name=Pen
```

---

## 🧪 Running Tests

```bash
python manage.py test
```

Includes tests for:

* CRUD operations
* Validation rules
* Error handling

---

## 🛡 Django Admin

Access admin panel:

```
http://127.0.0.1:8000/admin/
```

Admin features:

* Item list with visible columns
* Search & filtering
* Add / update / delete items

---

## 📝 Notes

* `venv/` and `.vscode/` are intentionally excluded via `.gitignore`
* SQLite is used for development
* API tested using Postman

---

## 👩‍💻 Author

**Shimra Foumy**
Backend Development Learning Project
Day 1 – Day 6

---


