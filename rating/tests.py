from django.test import TestCase
from .models import categories,technologies, Profile, Project
from django.contrib.auth.models import User
import datetime as dt

class categoriesTestCase(TestCase):
    def setUp(self):
        self.Test = categories(categories='Test')

    def test_instance(self):
        self.assertTrue(isinstance(self.Test,categories))

    def tearDown(self):
        categories.objects.all().delete()

    def test_save_method(self):
        self.Test.save_category()
        category = categories.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_method(self):
        self.Test.delete_category('Test')
        category = categories.objects.all()
        self.assertTrue(len(category)==0)

class technologiesTestCase(TestCase):
    def setUp(self):
        self.Tester = technologies(technologies='Tester')

    def test_instance(self):
        self.assertTrue(isinstance(self.Tester,technologies))

    def tearDown(self):
        technologies.objects.all().delete()

    def test_save_method(self):
        self.Tester.save_technology()
        technology = technologies.objects.all()self.Test = categories(categories='Test')
        self.assertTrue(len(technology)>0)

    def test_delete_method(self):
        self.Tester.delete_technology('Tester')
        technology = technologies.objects.all()
        self.assertTrue(len(technology)==0)
