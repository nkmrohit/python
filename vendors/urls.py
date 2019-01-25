
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from vendors import views

urlpatterns = [
    path('', views.list, name='vlist'),
    path('create/', views.create, name='vcreate'),
    path('detail/<int:vendor_id>', views.detail, name='vdetail'),
    path('update/<int:vendor_id>', views.update, name="vupdate"),
    path('delete/<int:vendor_id>',views.delete, name="vdelete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
