from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from . import views
from .views import custom_logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.base, name="base"),
    path('base/', views.base, name="base.html")
]
