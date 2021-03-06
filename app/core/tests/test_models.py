from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@adilreza.com'
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'adil@SELISE.CH'
        user = get_user_model().objects.create_user(email, 'useradil')
        self.assertEqual(user.email, email.lower())
