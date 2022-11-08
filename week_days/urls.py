from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.get_info_about_peple),
    path('<int:days>/', views.get_info_about_days_number),
    path('<days>/', views.get_info_about_days, name='days_name'),

]
