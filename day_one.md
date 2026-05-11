# Day 1: Introduction to Django & Setup

Welcome to Day 1 of learning Django!

## What is Django?
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.

## Today's Goals
1. Understand the Model-View-Template (MVT) architecture.
2. Learn the difference between a Django **Project** and a Django **App**.
3. Explore the basic project structure (`manage.py`, `settings.py`, `urls.py`).

## What We Covered Today

Here is a summary of the concepts and code we wrote today:

1. **Django Project & App Structure:**
   - Initialized the main Django project `core`.
   - Created our first app called `user_management`.
   - Connected the `user_management` app's URLs to the main `core/urls.py` using `include()`.

2. **Models & Database:**
   - Created a `Teacher` model inside `user_management/models.py`.
   - Explored different field types: `CharField`, `EmailField`, `IntegerField`.
   - Discussed field options like `primary_key`, `db_index`, and `unique`.
   - Wrote a `__str__` dunder method to make our model objects readable in the admin.

3. **Routing (URLs):**
   - Configured `urlpatterns` in both the project (`core/urls.py`) and the app (`user_management/urls.py`).
   - Mapped `/home/` to the main home view and `/user_management/` to the app's specific view.

4. **Views & QuerySets:**
   - Wrote functional views to handle web requests.
   - Used `Teacher.objects.filter()` to fetch data from the database.
   - Handled scenarios where data might not be found using basic conditional statements (`if not teacher:`).
   - Returned basic string responses using `HttpResponse`.

5. **Templates & Context:**
   - Used `render()` to connect a view to an HTML template (`index.html`).
   - Created a context dictionary (`data`) with teacher information and passed it to the front-end template for rendering.

Awesome job! Next, we'll continue exploring how to use the Django admin panel and build more dynamic templates.
