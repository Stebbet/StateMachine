import json

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserInfo, DiagramsModel

c = Client()


# Create your tests here.
class TestModals(TestCase):
    def test_login_modal(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)  # test the status code returned
        self.assertTemplateUsed(response, template_name='login.html')  # test the template used

    def test_login_modal_reverse(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)  # test the status code returned
        self.assertTemplateUsed(response, template_name='login.html')  # test the template used

    def test_register_modal(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    def test_register_modal_reverse(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)  # test the status code returned
        self.assertTemplateUsed(response, template_name='register.html')  # test the template used

    def test_login_failed(self):
        response = self.client.get('/login_failed')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='login_failed.html')

    def test_login_failed_modal_reverse(self):
        response = self.client.get(reverse('login_failed'))
        self.assertEqual(response.status_code, 200)  # test the status code returned
        self.assertTemplateUsed(response, template_name='login_failed.html')  # test the template used

    def test_register_failed(self):
        response = self.client.get('/register_failed')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register_failed.html')

    def test_register_failed_modal_reverse(self):
        response = self.client.get(reverse('register_failed'))
        self.assertEqual(response.status_code, 200)  # test the status code returned
        self.assertTemplateUsed(response, template_name='register_failed.html')  # test the template used

    def test_account_error(self):
        response = self.client.get('/account_error')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='account_error.html')

    def test_account_error_modal_reverse(self):
        response = self.client.get(reverse('account_error'))
        self.assertEqual(response.status_code, 200)  # test the status code returned
        self.assertTemplateUsed(response, template_name='account_error.html')  # test the template used

    def test_save_success(self):
        response = self.client.get('/save_success')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='save_success.html')

    def test_save_success_modal_reverse(self):
        response = self.client.get(reverse('save_success'))
        self.assertEqual(response.status_code, 200)  # test the status code returned
        self.assertTemplateUsed(response, template_name='save_success.html')  # test the template used

    def test_account_settings(self):
        response = self.client.get('/account_settings')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='account_settings.html')

    def test_account_settings_modal_reverse(self):
        response = self.client.get(reverse('account_settings'))
        self.assertEqual(response.status_code, 200)  # test the status code returned
        self.assertTemplateUsed(response, template_name='account_settings.html')  # test the template used

    def test_file_already_exists(self):
        response = self.client.get('/file_already_exists')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='file_already_exists.html')

    def test_file_already_exists_reverse(self):
        response = self.client.get(reverse('file_already_exists'))
        self.assertEqual(response.status_code, 200)  # test the status code returned
        self.assertTemplateUsed(response, template_name='file_already_exists.html')  # test the template used

    def test_imports(self):
        response = self.client.get('/imports')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='imports.html')

    def test_imports_reverse(self):
        response = self.client.get(reverse('imports'))
        self.assertEqual(response.status_code, 200)  # test the status code returned
        self.assertTemplateUsed(response, template_name='imports.html')  # test the template used

    def test_help(self):
        response = self.client.get('/help')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='help.html')

    def test_help_reverse(self):
        response = self.client.get(reverse('help'))
        self.assertEqual(response.status_code, 200)  # test the status code returned
        self.assertTemplateUsed(response, template_name='help.html')  # test the template used

    def test_about(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='about.html')

    def test_about_reverse(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)  # test the status code returned
        self.assertTemplateUsed(response, template_name='about.html')  # test the template used

    def test_privacy_policy(self):
        response = self.client.get('/privacy_policy')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='privacy_policy.html')

    def test_privacy_policy_reverse(self):
        response = self.client.get(reverse('privacy_policy'))
        self.assertEqual(response.status_code, 200)  # test the status code returned
        self.assertTemplateUsed(response, template_name='privacy_policy.html')  # test the template used

    def test_are_you_sure(self):
        response = self.client.get('/are_you_sure')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='are_you_sure.html')

    def test_are_you_sure_reverse(self):
        response = self.client.get(reverse('are_you_sure'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='are_you_sure.html')

    def test_delete_success(self):
        response = self.client.get('/delete_success')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='delete_success.html')

    def test_delete_success_reverse(self):
        response = self.client.get(reverse('delete_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='delete_success.html')


class LoginTests(TestCase):

    def setUp(self):
        User.objects.create(username='testuser', password='Hjguhjlkjbv765588').save()

    def test_url(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)  # test the status code returned
        self.assertTemplateUsed(response, template_name='login.html')  # test the template used

    def test_url_via_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)  # test the status code returned
        self.assertTemplateUsed(response, template_name='login.html')  # test the template used

    def test_login_form(self):
        response = self.client.post(reverse('login'), data={
            'username': 'testuser',
            'password': 'Hjguhjlkjbv765588'
        })  # create a request to login as a user using the login form
        self.assertEqual(response.status_code, 302)


class SignUpTests(TestCase):

    def test_url(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)  # test the status code returned
        self.assertTemplateUsed(response, template_name='register.html')  # test the template used

    def test_url_via_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)  # test the status code returned
        self.assertTemplateUsed(response, template_name='register.html')  # test the template used

    def test_signup_form(self):
        # create a request to sign-up as a user using the sign-up form
        response = self.client.post(reverse('register'), data={'username': 'testuser',
                                                               'email': 'testuser@email.com',
                                                               'password1': 'Hjguhjlkjbv765588',
                                                               'password2': 'Hjguhjlkjbv765588'
                                                               })
        users = User.objects.all()  # get all the users from the database
        self.assertEqual(response.status_code, 302)  # test the status code returned
        self.assertEqual(users.count(), 1)  # since this is the first user then there should only be 1 user


"""
class TestDiagrams(TestCase):

    def test_save_diagram(self):

        User.objects.create(username='testuser', password='testpassword').save()
        UserInfo.objects.create(user=User.objects.get(username='testuser'), class_id=0, is_teacher=False).save()

        # Login the user
        c.login(username='testuser', password='testpassword')

        user = UserInfo.objects.get(user=User.objects.get(username='testuser'))

        diagram_data = '{"title": "testTitle", "content": "{"content": "content"}", "image": "testImage"}'



        response = c.post('/save/', diagram_data, content_type="text/plain")
        self.assertEqual(response.status_code, 302)  # test the status code returned

        d = DiagramsModel.objects.all()

        self.assertEqual(DiagramsModel.objects.count(), 1)

        self.assertEqual(d.title, 'testTitle')
        self.assertEqual(d.content, {'content': 'testContent'})
        self.assertEqual(d.image, 'testImage')
        self.assertEqual(d.user_id, user.id)
"""
