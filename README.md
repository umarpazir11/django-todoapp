# Django Todo App

A simple Todo list application built with Django. This is a personal learning
project I built to understand Django's core building blocks — the
Model-View-Template (MVT) architecture, the ORM, URL routing, and the
built-in admin site — through a small, working, end-to-end feature.

## Features

- List, create, complete/uncomplete, and delete todos
- Server-rendered UI with Django templates
- Full CRUD management of todos through the built-in Django admin site
- SQLite database via the Django ORM

## Tech Stack

- Python 3.13
- Django 6.0.6
- SQLite

## Project Structure

```
django-learn/
├── manage.py            # Django's command-line utility
├── config/               # Project configuration (settings, root URLs, WSGI/ASGI)
└── todos/                 # The todos app
    ├── models.py          # Todo model
    ├── views.py           # List/create, toggle, delete views
    ├── urls.py             # App-level routes
    ├── admin.py            # Admin site registration
    └── templates/todos/   # HTML templates
```

## Getting Started

### Prerequisites

- Python 3.11+

### Installation

```bash
git clone <repo-url>
cd django-learn
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open:

- http://127.0.0.1:8000/ — the todo list
- http://127.0.0.1:8000/admin/ — the admin panel (run `python manage.py createsuperuser` first)

## What I Learned

- Django's Model-View-Template pattern, and how it maps (and doesn't map) to
  MVVM patterns from mobile development
- How Django's ORM turns a `Model` class into database tables and migrations
- Routing requests through `urls.py` to view functions
- Using the built-in Django admin for CRUD without writing extra code
