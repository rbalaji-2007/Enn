from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("delete-transaction/<int:pk>/", views.delete_transaction, name="delete_transaction"),
]