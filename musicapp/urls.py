from django.conf.urls import url
from . import views
import django

app_name = 'musicapp'

urlpatterns = [
    # url(r'^$', views.index, name = "index"),
    # url(r'^(?P<album_id>[0-9]+)/$', views.detail, name = "detail"),
    # url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name="favorite"),

    url(r'^$', views.indexView.as_view(), name = "index"),
    url(r'^(?P<pk>[0-9]+)/$', views.detailView.as_view(), name = "detail"),
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name="favorite"),

    # url(r'^aaa', views.example, name="example"),
]

#views.py에 있는 detail의 parameter album_id와 이름이 같아야 한다