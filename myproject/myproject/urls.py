from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/doc/', include('django.contrib.admindocs.urls')),  # ドキュメント
    path('admin/', admin.site.urls),  # 管理画面
    path('', include('todo.urls')),  # todoアプリケーションのurls.pyを含める
    # path('', include('todo.urls_classes')),  # クラスベースビューの例
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
