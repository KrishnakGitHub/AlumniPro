from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from AlumniPro import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),                 
    path('college/', include('college.urls')),
    path('social/', include('social.urls')), 
    path('',include('college.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
