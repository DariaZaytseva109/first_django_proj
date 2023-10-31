from django.urls import path, re_path

from store.views import index, catalog, good_id, archive, about, show_store, contact, log_in

urlpatterns = [
    path('main/', index, name='home'),
    path('main/<slug:store_slug>/', show_store, name='show_store'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('log_in/', log_in, name='log_in'),
    path('catalog/', catalog, name='catalog'),
    path('catalog/<int:good_id>/', good_id, name='good'),
    re_path(r"catalog/archive/(?P<year_archive>[12][90][0-9]{2})/", archive, name='archive')
    ]
