from django.conf import settings
from django.db import models

import logging
logger = logging.getLogger(__name__)


{% with class_name=app_name|capfirst|slice:":-1" %}

class {{class_name}}(models.Model):
	"""
	{{class_name}}
	"""

	def save(self, *args, **kwargs):
		"""
		Do stuff on save
		"""

		return super({{class_name}}, self).save(*args, **kwargs)

	def clean(self, *args, **kwargs):
		"""
		Extra validations
		"""

		return super({{class_name}}, self).clean(*args, **kwargs)

{% endwith %}