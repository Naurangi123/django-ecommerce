
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from ecommerce_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('products/',include('products.urls')),
    path('orders/',include('orders.urls')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)