from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name=admin),
    path('news/', include("news.urls")),
    path('register/', include('register.urls')),
    path('', include("movie.urls")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
