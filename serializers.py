{% with class_name=app_name|capfirst|slice:":-1" %}
from rest_framework import serializers
from models import {{class_name}}
from django.utils.translation import ugettext as _

class {{class_name}}Serializer(serializers.ModelSerializer):
    """
    Serializer for the {{class_name}} object
    """

    class Meta:
        model = {{class_name}}
        fields = []

{% endwith %}