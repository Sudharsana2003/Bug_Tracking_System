# Bug Tracking System

## 1. Creation Of API EndPoints and Database Design:
Reference Document:  
https://victopialabs-my.sharepoint.com/:x:/p/sudharsana/IQAlOOt47aJCSIgqfzi-Q92OAdRaJUXX_NhEpF_zmNUA9S4?e=ICajAs

---

## 2. Project Focus

### Topics Covered

1. Project Structure  
2. Features  
3. Installation & Setup  
4. Virtual Environment  
5. Installed Packages  
6. Running the Server  
7. API Architecture  
8. Models & Serializers  
9. API EndPoints (FBV, CBV, ViewSets)  
10. Create / Update / Delete Flow  
11. Authentication (Token + JWT)  
12. Permissions & Groups  
13. Pagination  
14. Search API (Q-Objects)  
15. CORS Handling  
16. JS Client (Port 8111)  
17. Python API Clients  
18. Future Enhancements  

---

## 1. Project Structure (Workspace Setup)

### 1.1 Create the Project Directory and Navigate

```bash
mkdir Bug_Tracking_System
cd Bug_Tracking_System
````

---

### 1.2 Create the Virtual Environment

```bash
python -m venv venv
```

---

### 1.3 Activate the Virtual Environment

```bash
venv\Scripts\activate
```

---

### 1.4 Open the Project in VS Code

```bash
code .
```

---

### 1.5 How to create django app in nested folders

```bash
mkdir apps
cd apps
```

---

### 1.6 Inside apps

> `--app-name` syntax is relative to the project root
> `..\` tells Python to find `manage.py` in the parent folder

```bash
python ..\manage.py startapp users
python ..\manage.py startapp projects
python ..\manage.py startapp bugs
python ..\manage.py startapp comments
```

---

### 1.7 Update config/settings.py and apps files in every model

Use full path format (example: `'apps.users'`)

```python
INSTALLED_APPS = [
    'apps.users',
    'apps.projects',
    'apps.bugs',
    'apps.comments',
]
```

---

### 1.8 Run server or migrations

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

![Project Structure](https://github.com/user-attachments/assets/3ae8d063-0280-4276-a6ea-deb08ae30dd2)

---

## 2. Installation & Setup, Installed Packages , Running the Server (2-6)

---

### 2.1 Use requirement.txt

```txt
django
djangorestframework
djangorestframework-simplejwt
django-cors-headers
psycopg2-binary
```

Install packages using:

```bash
pip install -r requirements.txt
```

---

### 2.2 Create Models and Add in settings.py

![Installed Apps](https://github.com/user-attachments/assets/3401fde6-e5fa-4d53-b1bd-b73660c86504)

---

### 2.3 Running the server

![Server Started](https://github.com/user-attachments/assets/9a36d714-caa8-449f-baf9-03b6dee42377)

![Browser Output](https://github.com/user-attachments/assets/f5ad83b9-ae0a-4988-8025-bc52f76c43ef)


