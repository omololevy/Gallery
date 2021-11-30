from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
 
re_path(r'^$',views.home,name='home'),
re_path(r'^filter/(\d+)',views.filter_location,name='filter_location'),
re_path(r'^search/', views.search_results,name='search_results')   ,
path('uploads',views.upload_picture,name="upload_picture")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
