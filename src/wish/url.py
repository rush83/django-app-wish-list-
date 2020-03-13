from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('<int:id>/edit', views.edit),
    path('<int:id>/granted', views.granted),
    path('<int:id>/delete', views.delete),
]