from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
urlpatterns = [
    path('', views.freelencing, name='freelencing'),
    path('voir_plus/detail/<int:pk>', views.voir_plus, name='voir_plus'),
]