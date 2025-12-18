# Item Master API

## Overview
This project is a **Django REST Framework API** for managing inventory items. It allows you to create, read, update, and delete items (CRUD operations) with proper validation and error handling.  

This version covers **Day 1–3** of development, including:

- Django project setup
- Item model creation
- CRUD APIs
- Basic input validation
- Error handling

> **Note:** Day 4 tasks (automatic date tracking, reorder logic, status endpoint, Azure deployment) are not included in this version.

---

## Technology Stack

- **Backend:** Python 3, Django, Django REST Framework (DRF)
- **Database:** SQLite (local)
- **API testing:** Postman or browser
- **Version control:** Git, GitHub

---

## Features (Day 1–3)

- **Create Item** – `POST /api/items/`
- **List All Items** – `GET /api/items/`
- **Get Single Item** – `GET /api/items/<id>/`
- **Update Item** – `PUT /api/items/<id>/update/`
- **Delete Item** – `DELETE /api/items/<id>/delete/`
- **Basic Validation** – required fields, unique constraints
- **Error Handling** – handles item not found and invalid data

---

## Project Structure

ItemMasterAPI/
├── config/ # Django project settings
├── items/ # Item Master app
│ ├── migrations/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
├── manage.py
├── venv/ # Python virtual environment (ignored in git)
└── README.md



---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YourUsername/ItemMasterAPI.git
cd ItemMasterAPI

```
2. Create virtual environment & activate
 ````
   python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
````
3. Install dependencies
 ```
pip install django djangorestframework
```
4. Apply database migrations
 ```
python manage.py makemigrations
python manage.py migrate
```

5. Run the server
```
python manage.py runserver
```

Access APIs at: http://127.0.0.1:8000/api/items/


| Endpoint                  | Method | Description     |
| ------------------------- | ------ | --------------- |
| `/api/items/`             | GET    | List all items  |
| `/api/items/`             | POST   | Create new item |
| `/api/items/<id>/`        | GET    | Get item by ID  |
| `/api/items/<id>/update/` | PUT    | Update item     |
| `/api/items/<id>/delete/` | DELETE | Delete item     |


Notes

-Database: SQLite is used locally; can be switched to MySQL/PostgreSQL for production.
-Validation: DRF serializers handle input validation.
-Testing: APIs can be tested using Postman or browser.


Next Steps (Future Development)

-Implement automatic date tracking (created_at / updated_at)
-Add reorder logic and alerts
-Create status change endpoint (Active / Inactive)
-Deploy API to Azure App Service



Author:
Shimra Foumy


   
   

