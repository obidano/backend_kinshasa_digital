from django.urls import path

from app_contacts import views

urlpatterns = [
    path('create', views.create_contact),
]
