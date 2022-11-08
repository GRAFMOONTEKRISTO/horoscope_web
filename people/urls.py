from django.urls import path
from . import views

urlpatterns = [
    path('people_detail/', views.get_info_about_people),
]
