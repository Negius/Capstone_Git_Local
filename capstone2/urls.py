from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('posts.urls', namespace='posts')),
    
]
if settings.DEBUG:
            urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
            urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
