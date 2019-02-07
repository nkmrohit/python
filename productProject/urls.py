
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import authUser.views
from crudbuilder import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('authUser.urls')),
    url('product/', include('products.urls')),
    url(r'^vendors/', include('vendors.urls')),
    url(r'^customers/', include('customers.urls')),
    url(r'superadmin', include('superadmin.urls')),
    url(r'crudtest', include('crudtest.urls')),
    url(r'^crud/',  include(urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
