from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.general_union_view, name='General View'),
    url(r'^all/$', views.all_stats, name='All Stats'),
    url(r'^s/(?P<server>.*)/(?P<interval_start>[0-9]+)/(?P<interval_stop>[0-9]+)/$',
        views.get_count, name='stats'),
    url(r'^r/(?P<r_server>.*)/(?P<r_interval>[0-9]+)/(?P<r_start>[0-9]+)/(?P<r_stop>[0-9]+)/$', 
        views.get_IC_counts_in_range, name='range stats'),
    url(r'^ir/(?P<server>[^/]+)/(?P<interval>[0-9]+)/(?P<start>[0-9]+)/(?P<stop>[0-9]+)/$',
        views.get_counts_interval_range, name='Interval Range'),
    url(r'^iur/(?P<interval>[0-9]+)/(?P<start>[0-9]+)/(?P<stop>[0-9]+)/$',
        views.get_union_counts_interval_range, name='Union Interval Range'),
 	url(r'^iurr/(?P<interval>[0-9]+)/$',
        views.get_union_counts_interval_range_recent, name='Union Interval Range'),
]
