from django.urls import path, include
from .views import home, contact

# Creat your urls here.
urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
]