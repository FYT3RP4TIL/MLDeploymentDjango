from django.urls import path
from . import views # from current directory import views.py
# giving paths to root node MLDep/urls.py

urlpatterns = [
    path('', views.Welcome),
]