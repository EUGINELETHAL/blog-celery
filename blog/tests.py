from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post


class EntryModelTest(TestCase):
    
    def test_string_representation(self):
        post = Post(title="My entry title")
        self.assertEqual(str(post), post.title)

class HomePageTests(TestCase):
    """Test whether our blog entries show up on the homepage"""

    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')



    def test_one_post(self):
        Post.objects.create(title='My entry title', content='1-body', author=self.user, slug="My entry title")
        response = self.client.get('/blog/')
        self.assertContains(response, 'My entry title')
        self.assertContains(response, '1-body')
        self.assertContains(response, "My entry title")

        

        

    # def test_two_entries(self):
    #     Entry.objects.create(title='1-title', body='1-body', author=self.user)
    #     Entry.objects.create(title='2-title', body='2-body', author=self.user)
    #     response = self.client.get('/')
    #     self.assertContains(response, '1-title')
    #     self.assertContains(response, '1-body')
    #     self.assertContains(response, '2-title')    

    def test_homepage(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200) 