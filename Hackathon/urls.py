from django.conf.urls import patterns, include, url

from hackathon_base.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
    # url(r'^$', 'Hackathon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^cpu', get_cpu_info),
    url(r'^ram', get_mem_info),
    url(r'^tasks', get_tasks_info),
    url(r'^swap', get_swap_info),
)