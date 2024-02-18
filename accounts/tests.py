from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import UserCreationForm

from accounts.forms import UserRegistrationForm
# Create your tests here.


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