import django_heroku
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEYの値はセッションデータを格納するキーの生成や、
# パスワードリセットトークンの生成などのセキュリティ上重要な部分で使われます
# プロジェクト毎に異なる値を使用し、漏洩しないように管理する必要があります
SECRET_KEY = '=9t-3@j2a_qxt&r2x5+k(wyi0qu#mra15fke%e2s$(nl@d)$$2'

# SECURITY WARNING: don't run with debug turned on in production!
# デバッグモード
# DEBUG = Trueの場合は、Django内部で例外が発生した際にデバッグ情報をレスポンスに含めます
DEBUG = True

# アクセスを許可するホスト名(IPアドレス)
# DEBUG = Falseの場合には設定が必要です
ALLOWED_HOSTS = []

# 内部IPアドレス一覧
# django-debug-toolbar等で使います
INTERNAL_IPS = ['127.0.0.1']


# Application definition
# 有効にするDjangoアプリケーション一覧
INSTALLED_APPS = [
    # 'jet.dashboard',
    # 'jet',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo',
    # 'debug_toolbar',
    # 'django_extensions',
]

# 有効にするDjangoミドルウェア一覧
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
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


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
# データベース接続設定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
# 言語、タイムゾーン、国際化の設定
LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# 静的ファイルのパスの設定
STATIC_URL = '/static/'

# Activate Django-Heroku.
django_heroku.settings(locals())