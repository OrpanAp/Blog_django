# 📝 Django Blog

A full-stack **Blog Management Web Application** built with **Python and Django**.

This project provides a complete blogging workflow including user authentication, blog post management, categories, comments, featured posts, image uploads, search, and a dedicated dashboard for managing content and users.

The application follows Django's **MVT architecture** and uses the Django ORM, built-in authentication system, ModelForms, template context processors, media handling, and Django's built-in admin interface.

---

## 🌐 Live Demo

**Live Application:**
https://devalex.pythonanywhere.com/

---

## ✨ Features

### 📰 Blog System

* Create, read, update, and delete blog posts
* Draft and Published post status
* Featured blog posts
* Blog categories
* SEO-friendly slug-based blog URLs
* Featured images for posts
* Short descriptions and full blog content
* Automatic timestamps for creation and updates
* Author association for every blog post

### 🔎 Blog Search

The application provides a search system that searches published posts by:

* Blog title
* Short description
* Blog content
* Author username
* Category name

Search uses Django's `Q` objects to combine multiple query conditions.

### 🗂️ Categories

Authenticated dashboard users can:

* View categories
* Create categories
* Edit categories
* Delete categories

Category names are automatically normalized by capitalizing the first letter.

### 💬 Comments

Authenticated users can comment on published blog posts.

Each comment stores:

* User
* Blog post
* Comment content
* Creation time
* Update time

The blog detail page also displays the total comment count.

### 👤 Authentication

The project uses Django's built-in authentication framework.

Users can:

* Register
* Login
* Logout
* Access authenticated dashboard functionality

Registration is implemented using a custom form based on Django's `UserCreationForm`.

### 📊 Dashboard

The project includes a dedicated dashboard for authenticated users.

Dashboard functionality includes:

* Blog statistics
* Category management
* Blog post management
* User management

The dashboard uses Django's `login_required` decorator to protect its views.

### 👥 User Management

Dashboard users can manage registered users through:

* User listing
* User creation
* User editing
* User deletion

Additional protection prevents non-superusers from editing or deleting superuser accounts.

### 🖼️ Image Uploads

Blog posts support featured image uploads.

Uploaded images are stored using a date-based directory structure:

```text
media/
└── uploads/
    └── YYYY/
        └── MM/
            └── DD/
```

This keeps uploaded media organized by upload date.

### 🎨 Responsive UI

The project uses Django templates together with:

* HTML
* CSS
* Bootstrap 4
* django-crispy-forms

`django-crispy-forms` is configured with the Bootstrap 4 template pack for form rendering.

---

# 🛠️ Technologies

## Backend

| Technology                    | Purpose                             |
| ----------------------------- | ----------------------------------- |
| **Python**                    | Programming language                |
| **Django 6.0.1**              | Web framework                       |
| **Django ORM**                | Database interaction                |
| **SQLite**                    | Development database                |
| **Django Authentication**     | Registration, login and permissions |
| **Django Forms / ModelForms** | Form handling and validation        |

## Frontend

| Technology              | Purpose                  |
| ----------------------- | ------------------------ |
| **HTML5**               | Page structure           |
| **CSS3**                | Styling                  |
| **Bootstrap 4**         | Responsive UI components |
| **django-crispy-forms** | Form rendering           |

## Media & Utilities

| Package     | Purpose                                   |
| ----------- | ----------------------------------------- |
| **Pillow**  | Image processing and `ImageField` support |
| **Black**   | Python code formatting                    |
| **SQLite3** | Local database                            |

The dependency versions are pinned in `requirements.txt`, including Django 6.0.1, Pillow 12.1.0, django-crispy-forms 2.5, and crispy-bootstrap4 2025.6.

---

# 🏗️ Project Architecture

The project is divided into several Django applications.

```text
Blog_django/
│
├── assignments/
│   ├── models.py
│   ├── admin.py
│   └── views.py
│
├── blog_main/
│   ├── forms.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
│
├── blogs/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── context_processors.py
│
├── dashboard/
│   ├── forms.py
│   ├── views.py
│   └── urls.py
│
├── templates/
│   ├── home.html
│   ├── blogs.html
│   ├── login.html
│   ├── register.html
│   ├── search_results.html
│   ├── post_by_category.html
│   └── dashboard/
│       └── ...
│
├── media/
│   └── uploads/
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🧩 Django Applications

## `blog_main`

The main project application handles the application's core pages and authentication flow.

Responsibilities include:

* Home page
* User registration
* User login
* User logout
* Main URL configuration
* Django project configuration

The project routes requests through `blog_main/urls.py`, including the home page, authentication endpoints, blog pages, category pages, search, dashboard, and admin interface.

---

## `blogs`

The `blogs` application contains the main blogging functionality.

### Models

It defines three primary models:

### `Category`

```text
Category
├── category_name
├── created_at
└── updated_at
```

Category names are unique and normalized when saved.

### `Blogs`

```text
Blogs
├── title
├── slug
├── category
├── author
├── featured_image
├── short_description
├── blog_body
├── status
├── is_featured
├── created_at
└── updated_at
```

Blog posts can have either:

```text
Draft
Published
```

The `category` and `author` fields use Django foreign-key relationships. Blog images use Django's `ImageField`.

### `Comment`

```text
Comment
├── user
├── blog
├── comment
├── created_at
└── updated_at
```

Comments are associated with both the authenticated user and the blog post.

---

# 📊 Dashboard Application

The `dashboard` application provides authenticated content-management functionality.

All dashboard views are protected using Django's:

```python
@login_required(login_url='login')
```

The dashboard provides CRUD operations for:

### Categories

```text
/categories/
/categories/add/
/categories/edit/<id>
/categories/delete/<id>
```

### Blog Posts

```text
/posts/
/posts/add/
/posts/edit/<id>
/posts/delete/<id>
```

### Users

```text
/users/
/users/add/
/users/edit/<id>
/users/delete/<id>
```

The dashboard also calculates the total number of categories and blog posts for the dashboard overview.

---

# 🔄 Blog Post Creation Flow

Creating a blog post follows this process:

```text
User
  │
  ▼
Dashboard
  │
  ▼
Add Blog Post Form
  │
  ▼
BlogPostForm Validation
  │
  ▼
Assign Logged-in User as Author
  │
  ▼
Save Blog Post
  │
  ▼
Generate Slug
  │
  ▼
Save Final Post
```

The dashboard uses `BlogPostForm`, accepts uploaded files through `request.FILES`, assigns the authenticated user as the author, and generates a slug using the title plus the database ID.

Example:

```text
My First Django Blog
```

becomes approximately:

```text
my-first-django-blog-12
```

where `12` is the database ID.

---

# 🔐 Authentication Flow

The project uses Django's built-in authentication system.

### Registration

Registration uses a custom form derived from:

```python
UserCreationForm
```

The registration form accepts:

* First name
* Last name
* Username
* Email
* Password
* Password confirmation

### Login

The login process uses Django's:

```python
AuthenticationForm
```

After successful authentication, the user is logged in through:

```python
auth.login(request, user)
```

and redirected to the dashboard.

### Logout

Logout is handled with Django's:

```python
auth.logout(request)
```

---

# 🔎 Search Logic

Search is implemented using Django's `Q` objects.

A search term can match:

```text
Blog title
       OR
Short description
       OR
Blog body
       OR
Author username
       OR
Category name
```

Only published posts are returned.

Conceptually:

```text
Search Term
     │
     ├── title
     ├── description
     ├── content
     ├── author
     └── category
          │
          ▼
   Published Posts
```

This logic is implemented in `blogs/views.py`.

---

# ⭐ Featured Posts

The home page separates published blog posts into:

```text
Featured Posts
        │
        ├── Main Featured Post
        ├── Additional Featured Posts
        │
        └── Other Published Posts
```

Featured posts are determined using:

```python
is_featured=True
```

and only published posts are displayed as featured content.

---

# 🌐 URL Structure

The main application exposes routes such as:

| URL               | Purpose           |
| ----------------- | ----------------- |
| `/`               | Home page         |
| `/blogs/search/`  | Blog search       |
| `/category/<id>/` | Posts by category |
| `/blogs/<slug>/`  | Blog detail       |
| `/register/`      | User registration |
| `/login/`         | User login        |
| `/logout/`        | User logout       |
| `/dashboard/`     | Dashboard         |
| `/admin/`         | Django admin      |

These routes are defined through the project's main URL configuration and included application URL configurations.

---

# 🗄️ Database

The development database is SQLite:

```text
db.sqlite3
```

Django's ORM handles database operations, relationships, validation, and migrations.

The main relationships are:

```text
User
 │
 ├───────────────┐
 │               │
 ▼               ▼
Blogs         Comments
 │               │
 │               │
 ▼               ▼
Category       Blogs
```

More specifically:

```text
User 1 ──────── * Blogs
User 1 ──────── * Comments
Category 1 ──── * Blogs
Blogs 1 ─────── * Comments
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/OrpanAp/Blog_django.git
cd Blog_django
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Apply database migrations

```bash
python manage.py migrate
```

---

## 5. Create an administrator

```bash
python manage.py createsuperuser
```

Follow Django's prompts to create your admin account.

---

## 6. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# 🛠️ Useful Django Commands

### Create migrations

```bash
python manage.py makemigrations
```

### Apply migrations

```bash
python manage.py migrate
```

### Create superuser

```bash
python manage.py createsuperuser
```

### Start development server

```bash
python manage.py runserver
```

### Open Django shell

```bash
python manage.py shell
```

### Check the project

```bash
python manage.py check
```

---

# 🔑 Django Admin

The project also uses Django's built-in administration interface.

Visit:

```text
http://127.0.0.1:8000/admin/
```

The admin interface provides management for:

* Categories
* Blog posts
* Comments
* About information
* Social connections
* Users and Django authentication data

The blog admin interface also provides search, list display, and inline editing for post status and featured state.

---

# 📌 About & Social Connections

The `assignments` application contains additional site information.

### `About`

Stores:

* Title
* Description
* Creation date
* Update date

The application restricts the admin interface so only one `About` record can be created.

### `SocialConnect`

Stores:

* Platform
* URL
* Creation date
* Update date

These values can be exposed globally through the custom context processor.

---

# 🌍 Global Template Context

The project uses custom Django context processors to make commonly used data available throughout templates.

### Categories

```python
get_categories()
```

provides:

```python
categories
```

### Social Connections

```python
get_socialConnects()
```

provides:

```python
socialConnects
```

This avoids repeatedly querying the same information inside individual views.

---

# 📁 Static & Media Files

Django separates static assets from user-uploaded media.

### Static files

```text
/static/
```

Configured using:

```python
STATIC_URL = '/static/'
```

### Media files

```text
/media/
```

Configured using:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

During development, Django serves uploaded media when `DEBUG=True`.

---

# 🧠 Django Concepts Demonstrated

This project demonstrates several important Django concepts:

* Django project/app architecture
* MVT architecture
* Django ORM
* Model relationships
* ForeignKey relationships
* ModelForms
* Custom forms
* Django authentication
* User registration
* Login/logout
* Authentication decorators
* CRUD operations
* Django messages framework
* File uploads
* ImageField
* Static files
* Media files
* URL routing
* Dynamic URL parameters
* Slugs
* QuerySets
* `Q` objects
* Template context processors
* Django admin customization
* Database migrations
* Bootstrap integration
* Crispy Forms

---

# 🔒 Security Notes

This repository is currently configured primarily as a development project.

Before deploying it to production, review the following:

### 1. Secret key

The current project settings contain a hard-coded Django `SECRET_KEY`.

For production, move it into an environment variable:

```python
import os

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
```

### 2. Debug mode

The current settings use:

```python
DEBUG = True
```

Production deployments should use:

```python
DEBUG = False
```

### 3. Allowed hosts

Configure:

```python
ALLOWED_HOSTS = [
    "your-domain.com",
]
```

### 4. Database

SQLite is suitable for development and small applications, but production deployments may require a production database such as PostgreSQL.

### 5. Media uploads

Uploaded files should be configured and served appropriately for the production environment.

---

# 🚀 Deployment

The project is currently available online through PythonAnywhere:

**https://devalex.pythonanywhere.com/**

For a production deployment, configure:

```text
DEBUG = False
```

and provide appropriate:

```text
SECRET_KEY
ALLOWED_HOSTS
DATABASE
STATIC_ROOT
MEDIA_ROOT
```

along with a production WSGI/web-server configuration.

---

# 🔮 Possible Future Improvements

Potential improvements for future versions include:

* Pagination for blog listings
* Rich text editor for blog content
* Author-specific post permissions
* User profile pages
* Like/favorite functionality
* Comment moderation
* Comment deletion/editing
* Post categories with slugs
* Tags
* Advanced search filters
* PostgreSQL support
* Environment-based configuration
* Automated tests
* Production static/media storage
* Improved authorization using Django permissions/groups
* API endpoints using Django REST Framework
* CI/CD with GitHub Actions

---

# 🤝 Contributing

Contributions are welcome.

### 1. Fork the repository

### 2. Clone your fork

```bash
git clone https://github.com/your-username/Blog_django.git
```

### 3. Create a feature branch

```bash
git checkout -b feature/your-feature
```

### 4. Make your changes

### 5. Commit your changes

```bash
git add .
git commit -m "Add your feature"
```

### 6. Push your branch

```bash
git push origin feature/your-feature
```

### 7. Open a Pull Request

---

# 👨‍💻 Author

**OrpanAp**

GitHub:
https://github.com/OrpanAp

Email:
[purificationalex90@gmail.com](mailto:purificationalex90@gmail.com)

---

# 📄 License

No explicit open-source license is currently specified in the repository.

If you intend to distribute or reuse this project publicly, consider adding an appropriate license such as MIT.

---

## ❤️ Built With

Built with:

**Python • Django • SQLite • Bootstrap • django-crispy-forms • Pillow**

Made with ❤️ using Django.
