from django.test import TestCase

# Create your tests here.


from http import HTTPStatus
from django.urls import reverse
from django.utils import timezone
from django.http.request import HttpRequest
from django.contrib.auth import get_user_model



from posts.models import Post
from posts.forms import PostCreationForm



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


class PostCreationTest(TestCase):


    def setUp(self):


        self.url = reverse('post_creation')
        self.template_name = 'posts/post_creation.html'
        self.form_class = PostCreationForm

        self.title = 'Sample Title Test'
        self.body = 'Sample Body for sample test'
        self.author = 'author'
    

    def test_post_creation_page_exists(self):
        

        response = self.client.get(self.url)

        self.assertTemplateUsed(response, self.template_name)
        self.assertEqual(response.status_code, HTTPStatus.OK)


        form = response.context.get('form', None)
        self.assertIsInstance(form, self.form_class)
    

    def test_post_creation_form_create_post(self):
        post_request = HttpRequest()
        post_request.user = baker.make(User)


        post_data = {
            'title':self.title,
            'body':self.body,
            #'author':self.author
        }

        post_request.POST = post_data

        form = self.form_class(post_request.POST)

        self.assertTrue(form.is_valid())

        post_obj = form.save(commit=False)
        self.assertIsInstance(post_obj, Post)

        post_obj.author = post_request.user
        post_obj.save()

        self.assertEqual(Post.objects.count(), 1)

