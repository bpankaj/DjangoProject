from django.conf.urls import patterns, include, url
from django.contrib import admin
# from django.conf import settings
# from django.conf.urls.static import static


# if not settings.DEBUG:
# 	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyFirstApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
)
