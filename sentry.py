import os

from raven import Client, fetch_git_sha
from raven_aiohttp import AioHttpTransport
from raven.contrib.sanic import Sentry
from sanic.exceptions import NotFound
from config import current_config

# @TODO: Figure out why defined these constants here? Remove if redundant
sentry_client = None
sentry = None


# Configures the sentry client for the entire app based on the environment
def configure_sentry(app, config=current_config):
    global sentry_client
    global sentry
    if config.SENTRY_ENABLED:
        sentry_config = {
            'dsn': config.SENTRY_DSN,
            'release': fetch_git_sha(os.path.abspath(os.path.dirname(__file__))),
            'transport': AioHttpTransport,
            'ignore_exceptions': [NotFound],
            'environment': config.ENVIRONMENT
        }
        # initialize the client for sentry, note that the `sentry_client` is just a base client
        # you should use the `client` for methods like captureMethod, captureException
        sentry_client = Client(**sentry_config)
        sentry = Sentry(app, client=sentry_client)
        app.sentry = sentry
        app.sentry_client = sentry_client
        return sentry
