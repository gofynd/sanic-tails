from .common import Config


class TestsConfig(Config):
    """Configuration for executing tests of this project"""
    ENVIRONMENT = 'test'
    MONGO_HOST = 'mongo'
    LOG_SETTINGS = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
        },
        'formatters': {
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': True
            },
        }
    }
