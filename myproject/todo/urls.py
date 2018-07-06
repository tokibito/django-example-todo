from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 一覧表示
    path('add', views.add, name='add'),  # 追加
    path('<int:pk>/edit', views.edit, name='edit'),  # 編集
    path('<int:pk>/done', views.done, name='done'),  # 完了
]
