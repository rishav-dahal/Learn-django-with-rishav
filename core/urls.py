from django.contrib import admin
from django.urls import path , include
from core import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('user_management/', include('user_management.urls')),
]
