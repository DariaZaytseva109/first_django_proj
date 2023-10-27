from django.urls import path, re_path

from store.views import index, catalog, good_id, archive

urlpatterns = [
    path('main/', index),
    path('catalog/', catalog),
    path('catalog/<int:good_id>/', good_id),
    re_path(r"catalog/archive/(?P<year_archive>[12][90][0-9]{2})/", archive)
]