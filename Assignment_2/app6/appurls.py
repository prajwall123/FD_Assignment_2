from django.urls import path
from .import views

urlpatterns=[
    path('',views.home),
    path('open_savings_account/<int:cus_id>/', views.openaccount, name='open_savings_account'),
]