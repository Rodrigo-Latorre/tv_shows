from functools import update_wrapper
from django.urls import path
from . import views
urlpatterns = [
    path('', views.register),
    path('shows/register/', views.register),
    path('shows/new/',views.new),
    path('shows/create/',views.create),
    path('shows/<id>/edit/', views.edit),
    path('shows/<id>/destroy/', views.destroy),
    path('shows/<id>/update/', views.update),
    path('shows/<id>/', views.shows_id),
    path('shows/', views.shows),
]
