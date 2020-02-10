from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class AvaliateUser(APITestCase):
    def test_avaliate_user():
