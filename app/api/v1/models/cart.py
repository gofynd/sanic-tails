import mongoengine as me
from marshmallow_mongoengine import ModelSchema


class Article(me.EmbeddedDocument):
    name = me.StringField(required=True)


class Cart(me.Document):
    user_id = me.IntField(required=True)
    articles = me.ListField(me.EmbeddedDocumentField(Article))


class User(me.Document):
    name = me.StringField(required=True)
    password = me.StringField(required=True)
    email = me.StringField(required=True)


# Declare Marshmallow Schemas
class ArticleSchema(ModelSchema):
    class Meta:
        model = Article


class CartSchema(ModelSchema):
    class Meta:
        model = Cart


class UserSchema(ModelSchema):
    class Meta:
        model = User
