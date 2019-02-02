from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from superadmin.adminauth import views

urlpatterns = [
    path('', views.list, name='adminlist'),
    #path('login/', views.login, name='vendorlogin'),
    #path('create/', views.create, name='vendorcreate'),
    #path('edit/', views.edit, name='vendorupdate'),
    #path('list/', views.list, name='vendorlist'),
    #path('detail/<int:cst_id>', views.detail, name="vendordetails"),
    #path('edit/<int:cst_id>', views.edit, name="vendoredit"),
    #path('delete/<int:cst_id>', views.delete, name="vendordelete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

