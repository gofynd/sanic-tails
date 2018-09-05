import logging
import json

from sanic.views import HTTPMethodView
from sanic import response
from marshmallow import ValidationError
from ..models.cart import User, UserSchema
from ...common.views.base_view_class import BaseViewClass


class UserView(BaseViewClass):
    """ Things you can do with a User """

    def get(self, request, *args, **kwargs):
        """ List the users
            ---
            summary: List User(s)
            description: Get all the users in the DB or a specific user by specified `id`
            tags:
                - user
            parameters:
                - name: id
                  in: query
                  description: Id of the particular User
                  type: integer
                  required: false
            responses:
                200:
                    description: List users
                    schema: UserSchema
                404:
                    description: User not found
        """
        logger = logging.getLogger(__file__)
        logger.info("In User view")
        return response.json(UserSchema(many=True).dump(User.objects.all()).data)

    def post(self, request, *args, **kwargs):
        """ Add a user
            ---
            summary: Insert a User
            description: Insert a User in the DB
            tags:
                - user
            parameters:
                - name: User
                  in: body
                  description: User object that needs to be added
                  schema: UserSchema
            responses:
                200:
                    description: Show Added User
                    schema: UserSchema
        """
        user_dict = json.loads(request.body)
        loaded_schema = UserSchema().load(user_dict)
        if loaded_schema.errors:
            return response.json(loaded_schema.errors)
        return response.json(UserSchema().dump(loaded_schema.data.save()).data)

    def put(self, request, *args, **kwargs):
        """ Add a user
            ---
            summary: Update a User
            description: Update an existing User in the DB
            tags:
                - user
            parameters:
                - name: id
                  in: query
                  description: Id of the particular User
                  type: integer
                  required: false
                - name: User
                  in: body
                  description: User object that needs to be updated
                  schema: UserSchema
            responses:
                200:
                    description: Show Added User
                    schema: UserSchema
                404:
                    description: User not found
        """
        user = User.objects.get(id=request.raw_args['id'])
        if not user:
            return response.json({'error': 'Invalid User'}, status=404)
        user_dict = json.loads(request.body)
        loaded_schema = UserSchema().load(user_dict)
        if loaded_schema.errors:
            return response.json(loaded_schema.errors)
        user.update(**user_dict)
        user = user.reload()
        return response.json(UserSchema().dump(user).data)

    def delete(self, request, *args, **kwargs):
        """ Delete a user
            ---
            summary: Remove a User
            description: Remove a user from the DB by their specified `id`
            tags:
                - user
            parameters:
                - name: id
                  in: query
                  description: Id of the particular User
                  type: integer
                  required: true
            responses:
                200:
                    description: User removed successfully
        """
        user = User.objects.get(id=request.raw_args['id'])
        user.delete()
        return response.json({'success': True})
