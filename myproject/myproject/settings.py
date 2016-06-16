import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECRET_KEYの値はセッションデータを格納するキーの生成や、
# パスワードリセットトークンの生成などのセキュリティ上重要な部分で使われます
# プロジェクト毎に異なる値を使用し、漏洩しないように管理する必要があります
SECRET_KEY = 'n)+_snr(y5-zty5ps4(755m5_wnsx3)yp8x^*o+n8m%io31%57'

# デバッグモード
# DEBUG = Trueの場合は、Django内部で例外が発生した際にデバッグ情報をレスポンスに含めます
DEBUG = True

# アクセスを許可するホスト名(IPアドレス)
# DEBUG = Falseの場合には設定が必要です
ALLOWED_HOSTS = []

# 有効にするDjangoアプリケーション一覧
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo',
]

# 有効にするDjangoミドルウェア一覧
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLディスパッチに使うルートモジュール
ROOT_URLCONF = 'myproject.urls'

# テンプレート設定
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGIアプリケーション設定
WSGI_APPLICATION = 'myproject.wsgi.application'

# データベース接続設定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 言語、タイムゾーン、国際化の設定
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 静的ファイルのパスの設定
STATIC_URL = '/static/'
