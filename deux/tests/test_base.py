from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class BaseUserTestCase(APITestCase):

    def simpleUserSetup(self):
        self.password1 = "password_1"
        self.user1 = User.objects.create_user(
            username="test1",
            email="test1@example.com",
            password=self.password1,
            first_name="Test",
            last_name="One")

        self.password2 = "password_2"
        self.user2 = User.objects.create_user(
            username="test2",
            email="test2@example.com",
            password=self.password2,
            first_name="Test",
            last_name="Two")

    def check_get_response(
            self, url, expected_status_code, data=None, user=None):
        self.client.force_authenticate(user)
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, expected_status_code)
        return response

    def check_post_response(
            self, url, expected_status_code, data=None, user=None,
            format="json", headers=None):
        headers = headers or {}
        self.client.force_authenticate(user)
        response = self.client.post(url, data=data, format=format, **headers)
        self.assertEqual(response.status_code, expected_status_code)
        return response

    def check_post_response_with_url_encoded(
            self, url, expected_status_code, data=None, user=None,
            headers=None):
        headers = headers or {}
        self.client.force_authenticate(user)
        response = self.client.post(
            url, data=data, content_type='application/x-www-form-urlencoded',
            **headers)
        self.assertEqual(response.status_code, expected_status_code)
        return response

    def check_put_response(
            self, url, expected_status_code, data=None, user=None,
            format="json"):
        self.client.force_authenticate(user)
        response = self.client.put(url, data=data, format=format)
        self.assertEqual(response.status_code, expected_status_code)
        return response

    def check_patch_response(
            self, url, expected_status_code, data=None, user=None,
            format="json"):
        self.client.force_authenticate(user)
        response = self.client.patch(url, data=data, format=format)
        self.assertEqual(response.status_code, expected_status_code)
        return response

    def check_delete_response(
            self, url, expected_status_code, user=None):
        self.client.force_authenticate(user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, expected_status_code)
        return response

    def check_options_response(
            self, url, expected_status_code, data=None, user=None,
            format="json"):
        self.client.force_authenticate(user)
        response = self.client.options(url, data=data, format=format)
        self.assertEqual(response.status_code, expected_status_code)
        return response
