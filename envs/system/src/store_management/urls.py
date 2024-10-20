from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('store_management/', views.store_management, name='store_management'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]

