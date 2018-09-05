import logging
from sanic import Sanic
from sentry import configure_sentry
from config import current_config
from sanic_prometheus import monitor
from mongoengine import connect


def create_app():
    app = Sanic(__name__, log_config=current_config.LOG_SETTINGS)
    configure_sentry(app)
    logger = logging.getLogger(__file__)
    logger.info("Server started successfully", {
                "text": "testing logging", "nested": {"more": "data"}})

    @app.listener('before_server_start')
    async def setup_db(app, loop):
        logger.info(
            'before server start...............setting up middleware, DB')
        connect('test_starscream')

    @app.listener('before_server_start')
    async def register_middleware(app, loop):
        logger.info(
            'before server start...............setting up middleware, blueprints')
        from app.api.routes.routes_v1 import api_v1_blueprint
        # @TODO: Implement attach_middleware(adds client's device info)
        # attach_middleware(app)
        app.blueprint(api_v1_blueprint)

    # adds /metrics endpoint to your Sanic server
    monitor(app).expose_endpoint()
    return app
