"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path('users/', views.employees_list, name='employees_list'),
    path('visit/<int:visit_id>', views.visit_detail, name='visit_detail'),
    path('salon/<int:salon_id>', views.salon_detail, name='salon_detail'),
    path('salon/', views.salon_list, name='salon_list'),
    path('visit/create/', views.create_visit, name='create_visit'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('newuser/', views.new_user, name='new_user'),
    path('users/<int:pk>', views.user_profile, name='user_profile'),
    path('passwdscc/', views.password_success, name='password_success'),
    path('password/', views.change_password, name='change_password'),
    path('calendar/<int:salon_id>', views.calendar_view, name='calendar'),
    path('newsalon/', views.new_salon, name='new_salon')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# statics not for production!!!
