from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<str:nombre>', views.get_content),
]
