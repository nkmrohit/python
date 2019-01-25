
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import authUser.views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('authUser.urls')),
    url('product/', include('products.urls')),
    url('vendors/', include('vendors.urls')),
    url(r'^customers/', include('customers.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
