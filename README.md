# 🎫 Event Tracker

A production-minded **full CRUD web application** for managing festivals and job applications. Built with **Django 6** and **Tailwind CSS 4**, it provides a secure, responsive interface to track events, applications, and hiring pipeline status in one place.

---

## ✨ Overview

**Event Tracker** helps users organize festivals (`Evento`) and monitor job applications (`Candidatura`) linked to each event. Every core operation — **Create, Read, Update, and Delete** — is implemented for both domain entities, with server-side validation, relational data integrity, and authenticated access throughout.

---

## 🏗 Architecture: Django MVT

This project follows Django's **Model–View–Template (MVT)** pattern, keeping concerns cleanly separated:

| Layer | Responsibility | Implementation |
|---|---|---|
| **Model** | Data schema & business rules | `eventos/models.py` — `Evento`, `Candidatura` |
| **View** | Request handling & logic | `eventos/views.py` — CRUD views, auth guards |
| **Template** | Presentation layer | `eventos/templates/` — HTML + Tailwind CSS |

**Request flow:**

```
Client → URL Router → View (logic) → Model (ORM) → PostgreSQL
                              ↓
                         Template (HTML response)
```

Views remain thin and focused: they validate input through `ModelForm` instances, delegate persistence to the ORM, and render templates with the appropriate context. URL routing is centralized in `config/urls.py`, following Django best practices.

---

## 🗄 Relational Database Design

The application uses **PostgreSQL** as its relational database engine, managed through Django's ORM and migration system.

### Entity Relationship

```
Evento (1) ──────────< (N) Candidatura
```

- **`Evento`** — Represents a festival or event (`nombre`, `lugar`, `fecha_inicio`, `fecha_fin`).
- **`Candidatura`** — Represents a job application tied to a single event via a **ForeignKey** with `CASCADE` deletion.

When an event is removed, all related applications are automatically deleted, preserving referential integrity at the database level.

### Application Status Workflow

Each `Candidatura` tracks its lifecycle through a constrained `choices` field:

| Status | Description |
|---|---|
| `ENVIADA` | Application submitted |
| `ENTREVISTA` | Interview in progress |
| `ACEPTADA` | Hired |
| `RECHAZADA` | Rejected |

Schema changes are version-controlled through Django migrations (`eventos/migrations/`).

---

## 🔐 Security

Security is enforced at multiple layers — not only at the UI.

### Authentication (`@login_required`)

Every application view is protected with Django's `@login_required` decorator. Unauthenticated users are redirected to `/accounts/login/` before accessing any CRUD endpoint.

Authentication is powered by **`django.contrib.auth`**, with session-based login and logout via built-in auth URLs.

### CSRF Protection

Cross-Site Request Forgery protection is enabled globally through:

- **`CsrfViewMiddleware`** in `config/settings.py`
- **`{% csrf_token %}`** on every POST form across templates

State-changing operations (create, update, delete) cannot be executed without a valid CSRF token bound to the user's session.

### Additional Hardening

- **Password validators** — Django's built-in validators enforce minimum complexity on user credentials.
- **Clickjacking protection** — `XFrameOptionsMiddleware` prevents the app from being embedded in unauthorized frames.
- **Server-side form validation** — All user input passes through `ModelForm.is_valid()` before reaching the database.

---

## 🛠 Tech Stack

| Technology | Role |
|---|---|
| **Django 6.0** | Web framework, ORM, auth, admin |
| **PostgreSQL** | Relational database |
| **Tailwind CSS 4** | Utility-first, responsive UI |
| **Node.js / npm** | CSS build pipeline |
| **Python 3.12+** | Runtime |

---

## 📋 Features

- ✅ Full **CRUD** for events and job applications
- ✅ Responsive UI with **Tailwind CSS** (mobile-first layouts)
- ✅ Session-based **authentication** (login / logout)
- ✅ **Django Admin** panel at `/admin/`
- ✅ Confirmation flow before deleting applications
- ✅ Reusable `ModelForm` classes with styled widgets

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- Node.js 20+
- PostgreSQL 14+

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/tracker_eventos.git
cd tracker_eventos
```

### 2. Set up the Python environment

```bash
python3 -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

### 3. Configure PostgreSQL

Create the database and user:

```sql
CREATE USER your_db_user WITH PASSWORD 'your_secure_password';
CREATE DATABASE tracker_db OWNER your_db_user;
GRANT ALL PRIVILEGES ON DATABASE tracker_db TO your_db_user;
```

Update `config/settings.py` with your credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tracker_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_secure_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

> ⚠️ For production, store credentials in environment variables — never commit secrets to version control.

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

All views require authentication. Create your first user:

```bash
python manage.py createsuperuser
```

### 6. Build frontend assets

```bash
npm install
npm run build:css
```

> `static/css/output.css` is gitignored and must be compiled after cloning.

### 7. Run the application

Use two terminals during development:

**Terminal 1 — Django dev server**

```bash
source venv/bin/activate
python manage.py runserver
```

**Terminal 2 — Tailwind watcher (optional, live CSS rebuild)**

```bash
npm run dev:css
```

Open **http://127.0.0.1:8000/** — you will be redirected to the login page.

---

## 🗺 API Routes

| Route | Method | Description | Auth |
|---|---|---|---|
| `/` | GET | Dashboard — list events & applications | 🔒 Required |
| `/accounts/login/` | GET/POST | User login | Public |
| `/accounts/logout/` | POST | User logout | 🔒 Required |
| `/añadir_evento/` | GET/POST | Create event | 🔒 Required |
| `/añadir_candidatura/` | GET/POST | Create application | 🔒 Required |
| `/eventos/<id>/editar/` | GET/POST | Update event | 🔒 Required |
| `/eventos/<id>/eliminar/` | GET | Delete event | 🔒 Required |
| `/candidaturas/<id>/editar/` | GET/POST | Update application | 🔒 Required |
| `/eliminar/<id>/` | GET/POST | Delete application (with confirmation) | 🔒 Required |
| `/admin/` | * | Django admin panel | 🔒 Staff only |

---

## 📁 Project Structure

```
tracker_eventos/
├── config/                     # Project configuration
│   ├── settings.py             # DB, middleware, auth, static files
│   └── urls.py                 # Root URL routing
├── eventos/                    # Main application
│   ├── models.py               # ORM models (Evento, Candidatura)
│   ├── views.py                # CRUD views + @login_required
│   ├── forms.py                # ModelForm classes
│   ├── admin.py                # Admin registration
│   ├── migrations/             # Database migrations
│   └── templates/
│       ├── eventos/            # App templates
│       └── registration/       # Login template
├── static/css/
│   ├── input.css               # Tailwind source
│   └── output.css              # Compiled CSS (generated)
├── manage.py
├── requirements.txt
├── package.json
└── .gitignore
```

---

## 📦 npm Scripts

| Command | Description |
|---|---|
| `npm run build:css` | One-time Tailwind CSS compilation |
| `npm run dev:css` | Watch mode — rebuilds CSS on file changes |

---

## 🚢 Production Checklist

Before deploying to production:

1. Set `DEBUG = False`
2. Rotate `SECRET_KEY` and load it from environment variables
3. Configure `ALLOWED_HOSTS`
4. Use environment variables for database credentials
5. Run `python manage.py collectstatic`
6. Compile assets with `npm run build:css`
7. Serve the app behind HTTPS with a production-grade WSGI server (e.g. Gunicorn)

---

## 📄 License

Open-source project. Add your preferred license (MIT, Apache 2.0, etc.).
