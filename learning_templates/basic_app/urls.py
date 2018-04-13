from django.conf.urls import url
from .views import *

app_name = 'basic_app'

urlpatterns = [
    url(r'other/', other, name='other'),
    url(r'relative/', relative, name='relative'),
]
