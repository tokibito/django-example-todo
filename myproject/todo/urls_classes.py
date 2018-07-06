from django.urls import path
from . import view_classes

urlpatterns = [
    path('', view_classes.Index.as_view(), name='index'),  # 一覧表示
    path('add', view_classes.Add.as_view(), name='add'),  # 追加
    path('<int:pk>/edit', view_classes.Edit.as_view(), name='edit'),  # 編集
    path('<int:pk>/done', view_classes.Done.as_view(), name='done'),  # 完了
]
