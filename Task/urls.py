from django.urls import path, include
from Task import views

urlpatterns = [
    path('', views.Foo, name = 'foo'),
]