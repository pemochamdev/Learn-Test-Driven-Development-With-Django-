from django.test import TestCase

# Create your tests here.

from posts.models import Post
import datetime
from http import HTTPStatus

class PostModelTest(TestCase):

    """ 
        Cette methode permet de savoir si un modele
        existe ou pas dans la BD
    # """
    # def test_model_exists(self):
    #     posts = Post.objects.count()

    #     self.assertEqual(posts, 0)
    

    def test_string_representation_of_object(self):
        post = Post.objects.create(
            title = "test",
            body = 'body',
            created_at = datetime.date,
            updated_at = datetime.date
        )

        post.save()

        self.assertEqual(post.title,  post.__str__())


class HomePageTest(TestCase):
    def setUp(self):
        Post.objects.create(
            title = "Simple test One",
            body = 'Simple Body One',

        )
        Post.objects.create(
            title = "Simple test Two",
            body = 'Simple Body Two',

        )
    

    def test_homepage_returns_correct_response(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'posts/home.html')
        self.assertEqual(response.status_code,HTTPStatus.OK)