from django.conf.urls import url, include
from django.contrib import admin
from rango.views import home, index, CategoryCreateView, CategoryUpdateView, CategoryDetailView

urlpatterns = [
    url(r'^create$', CategoryCreateView.as_view(), name="category_create"),
    url(r'^detail/(?P<pk>[0-9]+)/$', CategoryDetailView.as_view(), name="category_detail"),
    url(r'^update/(?P<pk>[0-9]+)/$', CategoryUpdateView.as_view(), name="category_update"),
]
