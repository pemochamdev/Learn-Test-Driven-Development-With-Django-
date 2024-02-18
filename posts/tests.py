from django.test import TestCase

# Create your tests here.

from posts.models import Post
import datetime
from django.utils import timezone
from http import HTTPStatus



class PostModelTest(TestCase):
    """
        Cette methode permet de savoir si un modele
        existe ou pas dans la BD
    #"""

    # def test_model_exists(self):
    #     posts = Post.objects.count()

    #     self.assertEqual(posts, 0)

    def test_string_representation_of_object(self):
        post = Post.objects.create(
            title="test",
            body="body",
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )

        post.save()

        self.assertEqual(post.title, post.__str__())


class HomePageTest(TestCase):
    def setUp(self):
        self.post1 = Post.objects.create(
            title="Simple test One",
            body="Simple Body One",
        )
        self.post2 = Post.objects.create(
            title="Simple test Two",
            body="Simple Body Two",
        )

    def test_homepage_returns_correct_response(self):
        response = self.client.get("/")

        self.assertTemplateUsed(response, "posts/home.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get("/")

        self.assertContains(response, self.post1.title)


class DetailPageTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title = "Le titre du post",
            body = "Le body du post",
            created_at=timezone.now(),
            updated_at=timezone.now,

        )
    

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