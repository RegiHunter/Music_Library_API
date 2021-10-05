DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'Mysql101!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}

SECRET_KEY = 'django-insecure-2776cyx(8_#or7^vlca_f=cq2_t*fw!qlcml_*hy_w-e21yn2g'

