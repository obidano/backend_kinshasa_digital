from django.urls import path

from app_contacts import views

urlpatterns = [
    path('create', views.create_contact),
    path('all', views.listing),
    path('update', views.update_contact),
    path('search', views.search),
    path('delete/<int:id>', views.delete_contact),
]
