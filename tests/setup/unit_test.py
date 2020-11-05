from myproject.settings import BASE_DIR
from django.test import TestCase
import selenium
import django
import os

class DependenciesInstalledTest(TestCase):
    
    def test_correct_version_of_django_is_installed(self):
        assert django.get_version() == '3.1.3'

    def test_correct_version_of_selenium_is_installed(self):
        assert selenium.__version__ == '3.141.0'


class DjangoConfigFilesTest(TestCase):
    
    def test_requirements_file_created(self):
        assert 'requirements.txt' in os.listdir(BASE_DIR)

    def test_pytest_ini_file_created(self):
        assert 'pytest.ini' in os.listdir(BASE_DIR)

    def test_django_project_created(self):
        assert 'manage.py' in os.listdir(BASE_DIR)


class GitTest(TestCase):

    def test_git_folder_created(self):
        assert '.git' in os.listdir(BASE_DIR)

    def test_git_ignore_created(self):
        assert '.gitignore' in os.listdir(BASE_DIR)


class DjangoWelcomePageTest(TestCase):

    def test_django_welcome_page_response_ok(self):
        response = self.client.get('/default-welcome-page/')
        assert response.status_code == 200


class DjangoAppTest(TestCase):

    def test_django_app_created(self):
        assert 'home' in os.listdir(BASE_DIR)