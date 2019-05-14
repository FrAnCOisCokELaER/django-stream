from template.settings.common import  *
import datetime

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

SECRET_KEY = os.environ.setdefault('DJANGO_SECRET_KEY', 'r^l&ak#w=g8=b&*d_7ow1sk89+3hzh#*#kf^e=cs#%u3=@npw*')

USE_X_FORWARDED_HOST= True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

PROXY = {}

ALLOWED_HOSTS.append(os.environ.setdefault('FQDN_HOST', 'testmobicloud.ifpen.com'))

JWT_SECRET_KEY = os.environ.setdefault('MOBICLOUD_JWT_SECRET_KEY', 'c64667fcace7d5a04cc8518b63b2f71a498ca539')

#security configuration
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}


JWT_AUTH = {
    'JWT_SECRET_KEY': JWT_SECRET_KEY,
    'JWT_ALGORITHM': 'HS512',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': False,
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_PAYLOAD_GET_USERNAME_HANDLER': 'template.jwt_custom_utils.jwt_get_username_from_payload_handler',
    'JWT_DECODE_HANDLER': 'template.jwt_custom_utils.jwt_decode_handler'
}

#logging configuration
LOGSTASH_HOST = os.environ.setdefault('LOGSTASH_HOST', 'testmobicloud.ifpen.com') 
LOGSTASH_PORT = os.environ.setdefault('LOGSTASH_PORT', '5000')

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
        'logstash': {
            'level': 'INFO',
            'class': 'logstash.TCPLogstashHandler',
            'host': LOGSTASH_HOST,
            'port': LOGSTASH_PORT, # Default value: 5959
            'version': 1, # Version of logstash event schema. Default value: 0 (for backward compatibility of the library)
            'message_type': 'template',  # 'type' field in logstash message. Default value: 'logstash'.
            #'fqdn': True, # Fully qualified domain name. Default value: false.
            'tags': ['template.request'], # list of tags. Default: None.
        },
  },
  'loggers': {
        'basiclogger': {
            'handlers': ['logstash','console'],
            'propagate': True,
            'level': 'INFO'
        },
    }
}

API_VERSION = os.environ.setdefault('API_VERSION', 'production-snapshot')

STATIC_ROOT = "/var/www/static/"

