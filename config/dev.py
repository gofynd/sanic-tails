from .common import Config


class DevelopmentConfig(Config):
    ENVIRONMENT = 'development'
    ALEXANDER_HOST = "http://localhost:8080"
    MONGO_HOST = 'localhost'
