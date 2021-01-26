from django.contrib import admin
from django.urls import path, include
from Task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Foo.as_view(), name = 'foo')
]
