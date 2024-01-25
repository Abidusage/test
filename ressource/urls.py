from django.urls import path
from . import views

urlpatterns = [
    path('', views.ressource, name="ressource"),
    path('ajouter', views.ajouter, name='ajouter'),
    path('delete_ressource/<int:pk>/', views.delete_ressource, name='delete_ressource'),
    path('update_ressource/<int:pk>/', views.update_ressource, name='update_ressource'),
    path('ressource/detail/<int:pk>/', views.detail, name="detail"),
    path('utilisateur', views.utilisateur, name='utilisateur'),
]