from django.test import TestCase

# Create your tests here.

from posts.models import Post
import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model
from http import HTTPStatus

"""
    le module bakery permet de creer les champs d'un model
    automatiquement:
    exemple: post = baker.make(Post) avec Post etant le modele
"""
from model_bakery import baker



User = get_user_model()

class PostModelTest(TestCase):
    """
        Cette methode permet de savoir si un modele
        existe ou pas dans la BD
    #"""

    # def test_model_exists(self):
    #     posts = Post.objects.count()

    #     self.assertEqual(posts, 0)

    def test_string_representation_of_object(self):
        post =baker.make(Post)
        post2  = baker.make(Post)
        post2.save()

        post.save()

        self.assertEqual(post.title, post.__str__())
        self.assertEqual(post2.title, post2.__str__())
        self.assertTrue(isinstance(post2, Post))


class HomePageTest(TestCase):
    def setUp(self):
        self.post1 =baker.make(Post)
        self.post2 =baker.make(Post)

    def test_homepage_returns_correct_response(self):
        response = self.client.get("/")

        self.assertTemplateUsed(response, "posts/home.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get("/")

        self.assertContains(response, self.post1.title)


class DetailPageTest(TestCase):
    def setUp(self):
        self.post = baker.make(Post)
    

    def test_detail_page_returns_correct_response(self):
        # response = self.client.get(f'post/{self.id}')
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'posts/detail.html')
    

    def test_detail_page_returns_correct_content(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)
        # self.assertContains(response, self.post.created_at)
        # self.assertContains(response, self.post.updated_at)
        self.assertTrue(response, self.post.created_at)


class ModelAuthorTest(TestCase):
    def setUp(self):
        self.user = baker.make(User)
        self.post = Post.objects.create(
            title = "Le titre",
            body = "Le body",
            author = self.user
        )
    
    def test_author_is_instance_of_user_model(self):
        self.assertTrue(isinstance(self.user, User))
    

    def test_post_belongs_to_user(self):
        self.assertEqual(self.post.author, self.user)
        self.assertTrue(hasattr(self.post, 'author'))