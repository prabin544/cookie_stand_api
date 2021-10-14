from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import CookieStand

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_CookieStand = CookieStand.objects.create(
            author = testuser1,
            title = 'Green Eggs and Ham',
            body = 'I do not like green eggs and ham, Sam I  am.'
        )
        test_CookieStand.save()

    def test_blog_content(self):
        CookieStand = CookieStand.objects.get(id=1)
        actual_author = str(CookieStand.author)
        actual_title = str(CookieStand.title)
        actual_body = str(CookieStand.body)
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_title, 'Green Eggs and Ham')
        self.assertEqual(actual_body, 'I do not like green eggs and ham, Sam I  am.')