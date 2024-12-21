# your_app/urls.py

from django.urls import path
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static function
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Home page (index.html)
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('services/', views.services, name='services'),  # Services page
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),  # Product detail page
    path('add_product/', views.add_product, name='add_product'),  # Add product page
    path('chat/', views.chat_page, name='chat_page'),
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
