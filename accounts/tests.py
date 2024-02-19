from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

from accounts.forms import UserRegistrationForm
# Create your tests here.

User = get_user_model()


class AccountCreationTest(TestCase):

    def setUp(self):

        self.form_class = UserRegistrationForm
    
    
    def test_signup_page_exists(self):
        url = reverse('signup')
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed('accounts/singup.html')
    

    def test_signup_form_works_correctly(self):
        

        
        self.assertTrue(issubclass(self.form_class, UserCreationForm))
        self.assertTrue('username' in self.form_class.Meta.fields)
        self.assertTrue('email' in self.form_class.Meta.fields)
        self.assertTrue('password1' in self.form_class.Meta.fields)
        self.assertTrue('password2' in self.form_class.Meta.fields)

        sample_data = {
            'username':'pmc',
            'email':'pmc@gmail.com',
            'password1':'Pmceohamdev#237',
            'password2':'Pmceohamdev#237'
        }

        form = self.form_class(sample_data)
        self.assertTrue(form.is_valid())
    

    def test_signup_form_create_user_in_db(self):


        user = {
            'username':'pmc',
            'email':'pmc@gmail.com',
            'password1':'Pmceohamdev#237',
            'password2':'Pmceohamdev#237'
        }

        form = self.form_class(user)

        if form.is_valid():
            form.save()
        
        self.assertEqual(User.objects.count(), 1)


class LoginTest(TestCase):

    def setUp(self):
        self.username = 'pmc'
        self.email = 'pmc@gmail.com'
        self.password = 'Pmc#237cmr'

        User.objects.create_user(
            username = self.username,
            email = self.email,
            password = self.password
        )

    def test_login_page_exists(self):
        
        url = reverse('login')
        response = self.client.get(url)

        self.assertTemplateUsed(response,'accounts/login.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)
    

    def test_login_page_has_login_form(self):
        url = reverse('login')
        response = self.client.get(url)

        form = response.context.get('form')

        self.assertIsInstance(form, AuthenticationForm)
    

    def test_login_page_logs_in_user(self):
        user_data = {
            'username ': self.username,
            'email ': self.email,
            'password ': self.password,
        }
        url = reverse('login')
        response = self.client.post(url, user_data)

        self.assertRedirects(response, reverse('home'))



class LogoutTest(TestCase):

    def setUp(self):
        self.username = 'pmc'
        self.email = 'pmc@gmail.com'
        self.password = 'Pmc#237cmr'

        User.objects.create_user(
            username = self.username,
            email = self.email,
            password = self.password
        )
    

    def test_logout_view_logs_out_user(self):
        self.client.login(
            username = self.username,
            password = self.password
        )

        self.assertTrue('_auth_user_id' in self.client.session)

        response = self.client.get(reverse('logout'))
        self.assertFalse('_auth_user_id' in self.client.session)
