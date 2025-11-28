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

```bash
    python manage.py makemigrations projects
    python manage.py migrate
```

## 14. User, Groups and Permissions

## 14.1 Creation of SuperUser
<img width="640" height="377" alt="Screenshot 2025-11-26 162152" src="https://github.com/user-attachments/assets/aaa50855-91fe-4adc-9635-d858d63920b8" />

## 14.2 Creation of Staffusers
<img width="1312" height="622" alt="image" src="https://github.com/user-attachments/assets/92e99fa5-b02b-425c-a9c2-9f1d7d581963" />

## 14.3 Creation of Manager, Reporter, Developer Group
     -Create users
     -map to each Group
     Below is my sample mapping of users to their roles:
<img width="1323" height="559" alt="image" src="https://github.com/user-attachments/assets/7c62daf3-c867-4a00-b407-45c82b3b5a17" />


## 14.4 Models

## 1.Models - Project
| User / Role                    | Permissions in Django                                | Can do in Admin              |
| ------------------------------ | ---------------------------------------------------- | ---------------------------- |
| **Superuser**                  | All                                                  | Add / Change / Delete / View |
| **Bala / Nithya (Manager)**    | Add / Change / Delete (via group)                    | Add / Change / Delete / View |
| **Kala / Surachi (Developer)** | View only (developers usually don't create projects) | View only                    |
| **Inba / Sri (Reporter)**      | View only                                            | View only                    |
| **Sudhir Normal user (no group)**     | View only                                            | View only                    |

## Operations -  Project:

## Admin
## 1.Creation/Updation/Deletion
<img width="1323" height="626" alt="image" src="https://github.com/user-attachments/assets/dca17ce4-26c3-40f9-b597-27b2250d9e0f" />
        

## Operations - Project

## Admin

### 1. Creation / Updation / Deletion

![Admin Operations](https://github.com/user-attachments/assets/dca17ce4-26c3-40f9-b597-27b2250d9e0f)

---

## 2. Model - Bug

### Model Creation and Migration

![Model Creation and Migration](https://github.com/user-attachments/assets/41611b16-31e1-4107-bc61-59dc255a696b)

---

## Operations - Bug

| Group     | Permissions                  |
| --------- | ---------------------------- |
| Admin     | All Bug permissions          |
| Manager   | Add / Change / Delete / View |
| Developer | Change Only assigned / View All                |
| Reporter  | Add / View                   |

- **Superuser / Admin / Manager**: Full control (create, assign, edit, delete)
- **Developer**: Can view, edit status/description, but cannot change assigned_to
- **Reporter**: Can create bugs, view everything, cannot assign or change priority

---

## Sample Output

### 1. Login As Reporter and Create a Bug

![Reporter Create Bug](https://github.com/user-attachments/assets/2ba9e5b9-9f4c-4add-adbe-dc4c07c19fc5)

![Reporter Bug View](https://github.com/user-attachments/assets/40018f76-188f-42fb-b50e-70731d06c262)

---

### 2. Manager Assigns the Reporter Bug to Developer

![Manager Assign Bug to Developer](https://github.com/user-attachments/assets/5be7881e-b116-438b-a39e-dc1c92bfe48e)

![Manager Bug Assigned](https://github.com/user-attachments/assets/44720ab7-725a-4813-9fd5-321e5dfc5e75)

---

### 3. Developer Modifies Priority and Sets Bug Status (Only Bugs Assigned to Them)

![Developer Modify Priority](https://github.com/user-attachments/assets/b390fd65-e8c7-4882-9376-e873df0f5144)

![Developer Modify Bug Status](https://github.com/user-attachments/assets/aec80e96-d2a1-4ebc-a4b7-8e609cb990ea)

---

## 3. Model - Comments

### Model Creation and Migration
![Comments Model Migration](https://github.com/user-attachments/assets/61ea2194-067a-4cc2-8f75-bcc9471b35a6)

---

## Operations - Comments

| Group     | Permissions                          |
| --------- | ------------------------------------ |
| Admin     | All Comment permissions              |
| Manager   | Add / Change / Delete / View         |
| Developer | Add / Change own comments / View all |
| Reporter  | Add / Change own comments / View all |

**Permission Highlights:**
- **Admin / Manager:** Full control (create, edit, delete, view)  
- **Developer / Reporter:** Can add and change only their own comments; can view all comments  

---

## Sample Output

**1. Manager assigning a comment on the bug of a project**  
![Manager Assign Comment](https://github.com/user-attachments/assets/7fc223c1-5739-4e89-bc9b-9eb0af56866b)

**2. Manager assigned a comment to a developer**  
![Manager Assigned to Developer](https://github.com/user-attachments/assets/74f44789-9ed4-4f5e-bac4-10cba7be0db8)

**3. Developer can see and update only their own comments, view others mapped to them**  
- Developer can update their own comment  
- Developer can only view comments from other users  


Absolutely! I can format all that data into clean **Markdown tables and notes**, following your sample style. Here's how it would look:

---

## Endpoints - Developer

### A. Bugs

| Action         | Endpoint                   | Expected Behavior                     |
| -------------- | -------------------------- | ------------------------------------- |
| List Bugs      | GET /api/bugs/             | Can view all bugs                     |
| Retrieve Bug   | GET /api/bugs/<bug_id>/    | Can view any bug                      |
| Create Bug     | POST /api/bugs/            | Typically NO                          |
| Update Bug     | PUT /api/bugs/<bug_id>/    | Can only update if assigned_to = self |
| Partial Update | PATCH /api/bugs/<bug_id>/  | Same as above                         |
| Delete Bug     | DELETE /api/bugs/<bug_id>/ | Not allowed                           |

* **Developer-specific**: Only allowed to update bugs assigned to them; cannot change `assigned_to`.

### B. Comments

| Action           | Endpoint                              | Expected Behavior               |
| ---------------- | ------------------------------------- | ------------------------------- |
| List Comments    | GET /api/comments/                    | Can view all comments           |
| Retrieve Comment | GET /api/comments/<comment_id>/       | Can view any comment            |
| Create Comment   | POST /api/comments/                   | Can add comments on any bug     |
| Update Comment   | PUT/PATCH /api/comments/<comment_id>/ | Only own comments (user = self) |
| Delete Comment   | DELETE /api/comments/<comment_id>/    | Not allowed                     |

* **Developer-specific**: Ownership enforced via `save_model` in admin and serializers.

### C. Projects

| Action               | Endpoint                        | Expected Behavior                |
| -------------------- | ------------------------------- | -------------------------------- |
| List Projects        | GET /api/projects/              | Can view all projects            |
| Retrieve Project     | GET /api/projects/<project_id>/ | Can view project details         |
| Create/Update/Delete | POST/PUT/PATCH/DELETE           | Not allowed (Admin/Manager only) |

---

## Endpoints - Manager

### A. Bugs

| Action         | Endpoint                   | Expected Behavior               |
| -------------- | -------------------------- | ------------------------------- |
| List Bugs      | GET /api/bugs/             | Can view all bugs               |
| Retrieve Bug   | GET /api/bugs/<bug_id>/    | Can view any bug                |
| Create Bug     | POST /api/bugs/            | Allowed                         |
| Update Bug     | PUT /api/bugs/<bug_id>/    | Can update any bug              |
| Partial Update | PATCH /api/bugs/<bug_id>/  | Allowed                         |
| Assign Bug     | PATCH /api/bugs/<bug_id>/  | Can assign bug to any developer |
| Delete Bug     | DELETE /api/bugs/<bug_id>/ | Allowed                         |

* **Manager-specific**: Full control over all fields including status, priority, `assigned_to`, due_date, severity.

### B. Comments

| Action           | Endpoint                              | Expected Behavior     |
| ---------------- | ------------------------------------- | --------------------- |
| List Comments    | GET /api/comments/                    | Can view all comments |
| Retrieve Comment | GET /api/comments/<comment_id>/       | Can view any comment  |
| Create Comment   | POST /api/comments/                   | Allowed               |
| Update Comment   | PUT/PATCH /api/comments/<comment_id>/ | Can edit any comment  |
| Delete Comment   | DELETE /api/comments/<comment_id>/    | Allowed               |

* **Manager-specific**: Full control over all comments.

### C. Projects

| Action           | Endpoint                              | Expected Behavior |
| ---------------- | ------------------------------------- | ----------------- |
| List Projects    | GET /api/projects/                    | Can view          |
| Retrieve Project | GET /api/projects/<project_id>/       | Can view          |
| Create Project   | POST /api/projects/                   | Allowed           |
| Update Project   | PUT/PATCH /api/projects/<project_id>/ | Allowed           |
| Delete Project   | DELETE /api/projects/<project_id>/    | Allowed           |

* **Manager-specific**: Owner/controller of project configuration.

---

## Endpoints - Reporter

### A. Bugs

| Action         | Endpoint                   | Expected Behavior                                 |
| -------------- | -------------------------- | ------------------------------------------------- |
| List Bugs      | GET /api/bugs/             | Can view all bugs                                 |
| Retrieve Bug   | GET /api/bugs/<bug_id>/    | Can view any bug                                  |
| Create Bug     | POST /api/bugs/            | Allowed, cannot assign (`assigned_to` auto blank) |
| Update Bug     | PUT /api/bugs/<bug_id>/    | Not allowed                                       |
| Partial Update | PATCH /api/bugs/<bug_id>/  | Not allowed                                       |
| Delete Bug     | DELETE /api/bugs/<bug_id>/ | Not allowed                                       |

* **Reporter-specific**: Cannot set `assigned_to`, status, priority, or severity.

### B. Comments

| Action           | Endpoint                              | Expected Behavior                |
| ---------------- | ------------------------------------- | -------------------------------- |
| List Comments    | GET /api/comments/                    | Can view all comments            |
| Retrieve Comment | GET /api/comments/<comment_id>/       | Can view any comment             |
| Create Comment   | POST /api/comments/                   | Allowed to add comment           |
| Update Comment   | PUT/PATCH /api/comments/<comment_id>/ | Only own comments                |
| Delete Comment   | DELETE /api/comments/<comment_id>/    | Not allowed for others’ comments |

* **Reporter-specific**: Own only the comments they create; cannot edit/delete others’ comments.

### C. Projects

| Action           | Endpoint                              | Expected Behavior        |
| ---------------- | ------------------------------------- | ------------------------ |
| List Projects    | GET /api/projects/                    | Can view all projects    |
| Retrieve Project | GET /api/projects/<project_id>/       | Can view project details |
| Create Project   | POST /api/projects/                   | Not allowed              |
| Update Project   | PUT/PATCH /api/projects/<project_id>/ | Not allowed              |
| Delete Project   | DELETE /api/projects/<project_id>/    | Not allowed              |

* **Reporter-specific**: Consumer only; cannot manage project configuration or assign bugs.

---

## Attached is the link to access the Postman workspace for the Bug Tracking System which includes:

    1.RBAC for CRUD Operations
    2.Pagination
    3.Search API using Q objects

[Postman Workspace](https://www.postman.com/docking-module-geoscientist-9348247/workspace/bug-tracking-system-django)

## CORS Handling

Cross-Origin Resource Sharing (CORS) is enabled to allow the frontend application to communicate with the Django REST API securely.

## Configuration

CORS is configured using the django-cors-headers package.

## Installation

```bash
pip install django-cors-headers
```

## Settings Configuration (settings.py)

```bash
INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8111",
]

CORS_ALLOW_CREDENTIALS = True
```


## Environment Setup

```md
The frontend JavaScript application is configured to communicate with the Django backend server running at:
```
[http://127.0.0.1:8000](http://127.0.0.1:8000)

```
Backend API is hosted locally on:
```
[http://localhost:8111](http://localhost:8111)

```
```

---





