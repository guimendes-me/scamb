from django.urls import path
from .views import home, logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('', home, name='home')
]