from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tutorials.urls')),  # Root URL goes to tutorials app
    path('users/', include('users.urls')),  # Users app
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)