from django.urls import path
from . import views

urlpatterns = [
    path('', views.postsite, name='postsite'),
    path('postsite_detail/<int:pk>/', views.postsite_detail, name='postsite_detail'),
    path('postsite_edit/<int:pk>/', views.postsite_edit, name='postsite_edit'),
    path('postsite_delete/<int:pk>/', views.postsite_delete, name='postsite_delete'),
]