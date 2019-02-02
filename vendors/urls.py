
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import authUser.views

urlpatterns = [

    url('auth/', include('vendorauth.urls')),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
