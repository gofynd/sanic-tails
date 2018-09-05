import os
from .dev import DevelopmentConfig
from .tests import TestsConfig

# Global statics (independent of environments) are to be defined in /config/common.py
APP_CONFIG_ENV = 'ALEXANDER_APP_CONFIG'

# Application wide config map
config = {
    'development': DevelopmentConfig,
    'tests': TestsConfig
}

# By default we set the config to development
config_name = os.environ.get(APP_CONFIG_ENV, 'development')
current_config = config.get(config_name)
print('config loaded for ', config_name)