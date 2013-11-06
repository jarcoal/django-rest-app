{% with class_name=app_name|capfirst|slice:":-1" var_name=app_name|slice:":-1" %}
from rest_framework import permissions
import models

class {{class_name}}Permissions(permissions.BasePermission):
    """
    Access rules for the {{class_name}} API
    """

    def has_permission(self, request, view):
    	"""
		Anonymous users can only retrieve a single record.
    	"""
    	return True

    def has_object_permission(self, request, view, {{var_name}}):
    	"""
		Permissions for singleton {{class_name}} objects
    	"""
        return True

{% endwith %}