import pytest
import logging
import json
from mongoengine import connect
from sanic import Sanic
from config import current_config
from app.api.routes.routes_v1 import api_v1_blueprint


def clear_database():
    from mongoengine.connection import _get_db
    db = _get_db()
    db.connection.drop()
    connect('test_starscream', host='mongo')


def create_test_app():
    """ We explicitly create test app as it may cause problems with global settings.
        See: https://github.com/yunstanford/pytest-sanic/issues/1
    """
    test_app = Sanic(__name__, log_config=current_config.LOG_SETTINGS)
    logger = logging.getLogger(__file__)
    logger.info("Server started successfully", {
                "text": "testing logging", "nested": {"more": "data"}})
    test_app.blueprint(api_v1_blueprint)
    connect('test_starscream', host=current_config.MONGO_HOST)
    return test_app


####################
# Factory & Helpers#
####################
def example_user():
    return {"name": "Wolf", "email": "wolf@example.com", "password": "1221111"}


def add_user_to_db():
    from app.api.v1.models.cart import UserSchema
    return str(UserSchema().load(example_user()).data.save().id)


#########
# Setup #
#########


@pytest.yield_fixture
def app():
    yield create_test_app()


@pytest.fixture
def test_cli(loop, app, test_client):
    return loop.run_until_complete(test_client(app))


#########
# Tests #
#########


async def test_list_users_fetches_all_users(test_cli):
    clear_database()
    add_user_to_db()
    resp = await test_cli.get('/api/v1/user')
    assert resp.status == 200
    resp_json = await resp.json()
    assert resp_json[0].items() >= example_user().items()


async def test_post_users_adds_the_user(test_cli):
    clear_database()
    resp = await test_cli.post('/api/v1/user', data=json.dumps(example_user()))
    assert resp.status == 200
    resp_json = await resp.json()
    assert resp_json.items() >= example_user().items()


async def test_put_users_updates_the_user(test_cli):
    clear_database()
    user_id = add_user_to_db()
    updated_user = example_user()
    updated_user.update({'name': 'Wolf Updated'})
    resp = await test_cli.put('/api/v1/user?id={}'.format(user_id), data=json.dumps(updated_user))
    assert resp.status == 200
    resp_json = await resp.json()
    assert resp_json.items() >= updated_user.items()


async def test_delete_users_removes_the_user(test_cli):
    clear_database()
    user_id = add_user_to_db()
    resp = await test_cli.delete('/api/v1/user?id={}'.format(user_id))
    assert resp.status == 200
    resp_json = await resp.json()
    assert resp_json == {'success': True}
