from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from customers.customerauth import views
from customerauth import views

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='custcreate'),
    path('edit/', views.edit, name='custupdate'),
    path('login/', views.login, name='custlogin'),
    path('list', views.list, name='list'),
    path('detail/<int:cst_id>', views.detail, name="details"),
    path('edit/<int:cst_id>', views.edit, name="custedit"),
    path('delete/<int:cst_id>', views.delete, name="delete"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

