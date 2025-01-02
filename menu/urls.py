from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.menu_view, name='menu'),  # Set up a default route
]
