from django.test import TestCase

import models
from django.core.urlresolvers import reverse

# Useful for fixtures:
# from django.contrib.webdesign.lorem_ipsum import words
# from django.utils.crypto import get_random_string

{{app_name}}_json = {
    
}

def create_{{app_name}}():
    return

{% with class_name=app_name|capfirst|slice:":-1" %}
class {{class_name}}Test(TestCase):
    def setUp(self):
        super({{class_name}}Test, self).setUp()
        self.list_url = reverse('{{app_name}}-list')
        self.detail_url = reverse('{{app_name}}-detail')

class TestApiList({{class_name}}Test):
    """
    GET /{{app_name}}
    """
    def test_anon(self):
        response = self.anonymous_client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

    def test_authenticated(self):
        response = self.authenticated_client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

class TestApiCreate({{class_name}}Test):
    """
    POST /{{app_name}}
    """
    def test_anon(self):
        "anon should not be able to create {{app_name}}"
        response = self.anonymous_client.post(self.list_url, self.bookable_json)
        self.assertEqual(response.status_code, 401)

    def test_authenticated(self):
        response = self.authenticated_client.get(self.list_url,
            self.bookable_json)
        self.assertEqual(response.status_code, 200)

class TestApiUpdate({{class_name}}Test):
    """
    PUT /{{app_name}}/:pk
    """

    def test_anon(self):
        "anon should not be able to update a single bookable"
        response = self.anonymous_client.put(self.detail_url)
        self.assertEqual(response.status_code, 401)

    def test_authenticated(self):
        response = self.authenticated_client.put(self.detail_url,
            self.bookable_json)
        self.assertEqual(response.status_code, 200)

class TestApiRetrieve({{class_name}}Test):
    """
    GET /{{app_name}}/:pk
    """

    def test_anon(self):
        response = self.anonymous_client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            # ...
        })

    def test_authenticated(self):
        response = self.authenticated_client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            # ...
        })

class TestApiDelete({{class_name}}Test):
    """
    DELETE /{{app_name}}/:pk
    """

    def test_anon(self):
        "anon should not be able to delete a single bookable"
        response = self.anonymous_client.delete(self.detail_url)
        self.assertEqual(response.status_code, 401)

    def test_authenticated(self):
        response = self.authenticated_client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
{% endwith %}