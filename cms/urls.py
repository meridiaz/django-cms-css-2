from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('css/', views.index_css),
    path('css/<str:nombre>', views.get_content_css),
    path('<str:nombre>', views.get_content),
]
