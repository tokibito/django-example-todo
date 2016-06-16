from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # 管理画面
    url('', include('todo.urls')),  # todoアプリケーションのurls.pyを含める
]
