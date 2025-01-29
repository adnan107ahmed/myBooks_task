from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('create-book/', views.create_or_update_book, name='create_book'),
    path('update-book/<int:book_id>/', views.create_or_update_book, name='update_book'),
]