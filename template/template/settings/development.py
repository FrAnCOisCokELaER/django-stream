from  template.settings.common import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r^l&ak#w=g8=b&*d_7ow1sk89+3hzh#*#kf^e=cs#%u3=@npw*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#Ifpen irproxy
PROXY = {
  'http': 'http://10.4.2.12:8082',
  'https': 'http://10.4.2.12:8082',
}

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
      'simple': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
  },
  'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
  },
  'loggers': {
        'basiclogger': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO'
        },
    }
}

API_VERSION = os.environ.setdefault('API_VERSION', 'development-snapshot')
