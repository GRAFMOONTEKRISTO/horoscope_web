from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area, name='path_rectangle'),
    path('square/<int:width>/', views.get_square_area, name='path_square'),
    path('circle/<int:radius>/', views.get_circle_area, name='path_circle'),
    path('get_rectangle_area/<int:width>/<int:height>/', views.get_rectangle),
    path('get_square_area/<int:width>/', views.get_square),
    path('get_circle_area/<int:radius>/', views.get_circle)

]
