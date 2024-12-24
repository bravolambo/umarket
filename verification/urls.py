from django.urls import path
from . import views

urlpatterns = [
    path('', views.verification_view, name='verification'),
]
