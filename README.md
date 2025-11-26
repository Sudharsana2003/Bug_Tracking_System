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
5. How to create django app in nested folders
6. Installed Packages  
7. Running the Server  
8. API Architecture  
9. Models & Serializers
10. Migrations
11. API EndPoints (FBV, CBV, ViewSets)  
12. Create / Update / Delete Flow  
13. Authentication (Token + JWT)  
14. Permissions & Groups  
15. Pagination  
16. Search API (Q-Objects)  
17. CORS Handling  
18. JS Client (Port 8111)  
19. Python API Clients  
20. Future Enhancements  

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

### 5. How to create django app in nested folders

### 5.1 How to create django app in nested folders

```bash
mkdir apps
cd apps
```

---

### 5.2 Inside apps

> `--app-name` syntax is relative to the project root
> `..\` tells Python to find `manage.py` in the parent folder

```bash
python ..\manage.py startapp users
python ..\manage.py startapp projects
python ..\manage.py startapp bugs
python ..\manage.py startapp comments
```

---

### 5.3 Update config/settings.py and apps files in every model

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

### 7. Running the server

![Server Started](https://github.com/user-attachments/assets/9a36d714-caa8-449f-baf9-03b6dee42377)

![Browser Output](https://github.com/user-attachments/assets/f5ad83b9-ae0a-4988-8025-bc52f76c43ef)


## 9. Connect to main URL Config and Migrations

<img width="640" height="377" alt="Screenshot 2025-11-26 162152" src="https://github.com/user-attachments/assets/d7075a4d-4a38-47a6-b150-ac9f420b6d88" />

python manage.py makemigrations projects
python manage.py migrate


## 14. User, Groups and Permissions

## 14.1 Creation of SuperUser
<img width="640" height="377" alt="Screenshot 2025-11-26 162152" src="https://github.com/user-attachments/assets/aaa50855-91fe-4adc-9635-d858d63920b8" />

## 14.2 Creation of Staffusers
<img width="1312" height="622" alt="image" src="https://github.com/user-attachments/assets/92e99fa5-b02b-425c-a9c2-9f1d7d581963" />

## 14.3 Creation of Manager Group
     -Create users
     -map to Manager Group
<img width="1323" height="559" alt="image" src="https://github.com/user-attachments/assets/7c62daf3-c867-4a00-b407-45c82b3b5a17" />


## Models

1.Project
| User / Role                    | Permissions in Django                                | Can do in Admin              |
| ------------------------------ | ---------------------------------------------------- | ---------------------------- |
| **Superuser**                  | All                                                  | Add / Change / Delete / View |
| **Bala / Nithya (Manager)**    | Add / Change / Delete (via group)                    | Add / Change / Delete / View |
| **Kala / Surachi (Developer)** | View only (developers usually don't create projects) | View only                    |
| **Inba / Sri (Reporter)**      | View only                                            | View only                    |
| **Sudhir Normal user (no group)**     | View only                                            | View only                    |


<img width="1323" height="626" alt="image" src="https://github.com/user-attachments/assets/dca17ce4-26c3-40f9-b597-27b2250d9e0f" />

     



