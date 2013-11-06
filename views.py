{% with class_name=app_name|capfirst|slice:":-1" %}
from rest_framework import viewsets
from serializers import {{class_name}}Serializer
from permissions import {{class_name}}Permissions
from models import {{class_name}}

# Utils
# from rest_framework import decorators
# from rest_framework.response import Response

class {{class_name}}ViewSet(viewsets.ModelViewSet):
    """
    {{class_name}} API Resource
    """
    serializer_class = {{class_name}}Serializer
    permission_classes = ({{class_name}}Permissions,)

    def get_queryset(self):
        qs = {{class_name}}.objects.all()

        # perform filters

        return qs

{% endwith %}