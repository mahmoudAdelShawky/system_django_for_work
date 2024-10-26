from . import views
from django.urls import path ,include
from django.contrib.auth.views import  LoginView
urlpatterns = [
    
    path('/login', LoginView.as_view(template_name='login.html') ,name='login'),
    path('/logout', views.logout_view, name='logout'),
    path('/signup', views.signup_view, name='signup'),
    path('/profile', views.profile, name='profile'),
    path('auth/', include('social_django.urls', namespace='social')), 
]

