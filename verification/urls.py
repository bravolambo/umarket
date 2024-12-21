from django.urls import path
from . import views

urlpatterns = [
    path('', views.verification_view, name='verification'),  # No prefix here
    path('success/', views.verification_success, name='verification-success'),
]
