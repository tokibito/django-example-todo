from django.conf.urls import url
from . import view_classes

urlpatterns = [
    url(r'^$', view_classes.Index.as_view(), name='index'),  # 一覧表示
    url(r'^add$', view_classes.Add.as_view(), name='add'),  # 追加
    url(r'^(?P<pk>\d+)/edit$', view_classes.Edit.as_view(), name='edit'),  # 編集
    url(r'^(?P<pk>\d+)/done$', view_classes.Done.as_view(), name='done'),  # 完了
]
