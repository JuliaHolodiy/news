from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'HotelApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'MyProject.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^register/', include('registr.urls')),
    url(r'^news/', include('news.urls', namespace='news')),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^register/$', RegisterFormView.as_view()),
    # url(r'^login/$', LoginFormView.as_view()),
    # url(r'^exit/$', LoginFormView.as_view()),
]