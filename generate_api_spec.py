import json

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from sanicplugin import SanicPlugin
from app.api.v1.views.cart_view import UserView
from app.api.v1.models.cart import UserSchema

# @TODO: Add tests in CI for successful generation of APISpec file
# Create spec object
spec = APISpec(
    title='StarScream',
    version='1.0.0',
    openapi_version='2.0',
    info=dict(
        description='Check status by pinging the server'
    ),
    plugins=[MarshmallowPlugin(), SanicPlugin()]
)

# Add tags
spec.add_tag(
    {"name": "user", "description": "Everything you can do with a user"})
# Add definitions
spec.definition('User', schema=UserSchema)
# Add views to generate paths for
user_view = UserView.as_view('user')
spec.add_path(path='/user', view=user_view)

# Save this generated spec to a file for now.
with open('swagger.json', 'w') as f:
    json.dump(spec.to_dict(), f)
