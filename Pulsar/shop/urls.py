from django.urls import path

from .views import *


urlpatterns = [
    path('all_orders/', ProductView.as_view()),
    path('<str:prod_name>/', ProductByNameView.as_view()),
]