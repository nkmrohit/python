from django.urls import path
from django.contrib import  admin
from django.conf.urls.static import static
from django.conf import settings
from . import views
from crudbuilder import urls
from django.conf.urls import include, url


urlpatterns = [
    path('', views.index, name='home'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^crud/',  include(urls)),
]   