from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class AuthTests(TestCase):
    def test_register_and_profile_created(self):
        resp = self.client.post(reverse('blog:register'), {
            'username':'tester',
            'email':'t@test.com',
            'password1':'StrongPassword123!',
            'password2':'StrongPassword123!'
        })
        self.assertEqual(resp.status_code, 302)
        user = User.objects.get(username='tester')
        self.assertIsNotNone(user.profile)  # profile created
