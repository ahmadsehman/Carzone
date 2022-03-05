from django.urls import path
from . import views

urlpatterns = [
    path('inquiry', views.inquiry, name='con_inquiry')
]