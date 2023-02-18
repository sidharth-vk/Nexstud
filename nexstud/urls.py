
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import handler404



handler404 = 'nexstud.views.handler404'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('', include('account.urls')),
    path('university/', include('university.urls')),
    path('blog/', include('blog.urls')),
    path('dashboard/', include('dashboard.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

