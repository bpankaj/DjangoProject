from django.conf.urls import patterns, url
from rango import views
# from django.conf import settings

# if settings.DEBUG:
# 	urlpatterns += patterns(
# 		'django.views.static',
# 		(r'^media/(?P<path>.*)',
# 		'serve',
# 		{'document_root': settings.MEDIA_ROOT}),)

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	#url(r'^about/$', views.about, name='about'),
	#url(r'^index', views.index, name='index'),
	url(r'^add_category/$', views.add_category, name='add_category'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^restricted/$', views.restricted, name='restricted'),
	url(r'logout/$', views.user_logout, name='logout'),
	)
