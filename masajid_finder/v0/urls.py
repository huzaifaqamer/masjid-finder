from django.urls import path

from . import views

urlpatterns = [
    path('mosques', views.FindMosques.as_view(), name='find-mosques'),
]