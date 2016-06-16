from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  # 一覧表示
    url(r'^add$', views.add, name='add'),  # 追加
    url(r'^(?P<pk>\d+)/edit$', views.edit, name='edit'),  # 編集
    url(r'^(?P<pk>\d+)/done$', views.done, name='done'),  # 完了
]
