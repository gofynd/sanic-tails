from sanic.views import HTTPMethodView
from .method_view_type import MethodViewType


class BaseViewClass(HTTPMethodView, metaclass=MethodViewType):
    pass
