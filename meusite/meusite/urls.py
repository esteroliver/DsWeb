from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('enquetes/', include('enquetes.urls')),
    path('', include('raiz.urls')),
    path('acervodigital/', include('acervodigital.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)