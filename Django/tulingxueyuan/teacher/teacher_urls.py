from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'tulingxueyuan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # 比如约定,凡是由teacher模块处理的视图的url都要以teacher开头
    #url(r'^teacher/', include(teacher_urls)),

    url(r'liudana/', views.do_app),
]