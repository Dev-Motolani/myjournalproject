from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:title_id>/', views.journal_detail, name='details'),
    path('add-title/', views.add_title, name='add_title'),
    path('add-entry/', views.add_entry, name='add_entry'),
    path('edit-title/<int:title_id>/', views.edit_title, name='edit_title'),
    path('edit-entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('delete-title/<int:title_id>/', views.delete_title, name='delete_title'),
    path('delete-entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]