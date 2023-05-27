"""
Django settings for django_ECG project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# print("----------")
# print(BASE_DIR)
# print("----------")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@i#e!y!burbv@lh0$)5hl*ossqramva&@4s%uai+r@iss-4$x4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



#增加系统导包路径
import sys
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# Application definition
INSTALLED_APPS = [
    'simpleui',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    # 'django_toolbar',
    'django_sslserver2',
    'rest_framework',
    # 'smart_chart.echart'
    'ckeditor',
    'ckeditor_uploader',
    
    'hospital',
    'patient',
    'model_classification',

]

MIDDLEWARE = [
    # 'django_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',



]
# ALLOWED_HOSTS = ["0.0.0.0","localhost","ecg.sjtu.edu.cn","10.168.94.244"]
# ALLOWED_HOSTS = ["ecg.sjtu.edu.cn"]
ALLOWED_HOSTS = ["*",]

#提供跨域访问功能
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

# ORS_ORIGIN_WHITELIST = (
#     'http://127.0.0.1:8080',
#     'http://localhost:8080',
#     'http://ecg.sjtu.edu.cn:8080',
#     'http://10.168.94.244:8080',
# )
ORS_ORIGIN_WHITELIST = (
    '*',
)



CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)

#
# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
# ]


ROOT_URLCONF = 'django_ECG.urls'

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

WSGI_APPLICATION = 'django_ECG.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}

# DDATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'bme', #数据库名字
#         'USER': 'postgres', #用户名
#         "PASSWORD" : 'bme123456', #自己的密码
#         "HOST":'localhost',
#         'PORT':5432,
#         # 'OPTIONS': {
#         #     'options': '-c search_path=myapp'
#         # }
#     }
# }
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
# LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False # 这里务必调整为False，否则时区设置无效
# USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

#django-simpleui配置
# 导入导出
IMPORT_EXPORT_USE_TRANSACTIONS = True

DEBUG = True
# 定义静态资源位置
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
     os.path.join(BASE_DIR, "/static/"),
 ]

SIMPLEUI_STATIC_OFFLINE = True # 离线模式
SIMPLEUI_HOME_INFO = False
SIMPLEUI_ANALYSIS = False
SIMPLEUI_ICON = {
    '患者名单': 'fa fa-address-book',
    # '模型': 'fa fa-bar-chart',
    # "医院名单" : 'fa fa-hospital-o',
    "医院名单" : 'fa fa-ambulance',
}
# MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')
# MEDIA_URL = 'upload/' #这个是在浏览器上访问该上传文件的url的前缀


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#富文本编辑器

CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_UPLOAD_PATH = os.path.join(BASE_DIR, "/static/upload/")