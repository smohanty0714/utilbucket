from django.urls import path

from . import views

urlpatterns = [
    path('ajax/convert_query/', views.covert_query, name='covert_query'),
    path('', views.index, name='index'),
]