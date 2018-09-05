from apispec.utils import load_operations_from_docstring, load_yaml_from_docstring
from apispec import BasePlugin


# @TODO: Support extracting paths from Blueprint and extract docstrings from views
class SanicPlugin(BasePlugin):

    def init_spec(self, spec):
        super(SanicPlugin, self).init_spec(spec)
        self.openapi_major_version = spec.openapi_version.major

    # @TODO: Implement a method that extracts path from the given view and raises error on failure to do so
    def path_helper(self, operations, view, **kwargs):
        """Path helper that allows passing a Sanic view function."""
        operations_from_docs = load_operations_from_docstring(view.__doc__)
        # Operation is specified in OpenAPI specifications
        # Refer: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#operation-object
        if operations_from_docs:
            operations.update(operations_from_docs)
        for method in view.view_class.methods:
            method_name = method.lower()
            method = getattr(view.view_class, method_name)
            method_operation = load_yaml_from_docstring(method.__doc__)
            if method_operation:
                operations[method_name] = load_yaml_from_docstring(
                    method.__doc__)
