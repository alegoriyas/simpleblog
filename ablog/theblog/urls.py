"""
Definition of urls for theblog.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
]
