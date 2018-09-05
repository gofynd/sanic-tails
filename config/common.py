import logging


class Config(object):
    DEBUG = True
    SENTRY_ENABLED = False
    SENTRY_DSN = ''
    SENTRY_LEVEL = logging.ERROR
    # @TODO: Make `simple` formatter display all the keys supported by JsonFormatter
    LOG_SETTINGS = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'rotating_log_handler': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': '/var/log/fynd/server.log',
                'maxBytes': 1024 * 1024 * 50,
                'backupCount': 10,
                'formatter': 'simple'
            },
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
                'handlers': ['rotating_log_handler', 'console'],
                'propagate': True
            },
        }
    }
