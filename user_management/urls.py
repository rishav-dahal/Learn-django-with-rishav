from django.urls import path

from user_management import views

urlpatterns = [
    path('', views.home, name='home'),
]
