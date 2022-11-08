from django.urls import path
from . import views

urlpatterns = [
    path('guinness/', views.get_guinness_world_records),
    path('actor/', views.get_info_about_actor),
    path('type/', views.html_about_four_elements),
    path('type/<str:sign_element>/', views.get_info_about_four_elements, name='elements_name'),
    path('', views.index, name='horoscope_index'),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope_name'),

]
