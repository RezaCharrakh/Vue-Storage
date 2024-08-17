import pytest
from django.test import TestCase
from objects_app.forms import CustomUserForm, ObjectForm
from objects_app.models import CustomUser, Object
import uuid


@pytest.mark.django_db
class TestCustomUserForm(TestCase):

    # def test_valid_custom_user_form(self):
    #     form_data = {
    #         'username': 'testuser',
    #         'email': 'test@example.com',
    #         'accessed_objects': [],
    #     }
    #     form = CustomUserForm(data=form_data)
    #     self.assertTrue(form.is_valid(), form.errors)

    def test_invalid_custom_user_form(self):
        form_data = {
            'username': '',  # Empty username should raise validation error
            'email': 'invalid_email',  # Invalid email format
            'accessed_objects': [999],  # Invalid object ID
        }
        form = CustomUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('accessed_objects', form.errors)

    # def test_custom_user_form_save(self):
    #     form_data = {
    #         'username': 'testuser',
    #         'email': 'test@example.com',
    #         'accessed_objects': [],
    #     }
    #     form = CustomUserForm(data=form_data)
    #     self.assertTrue(form.is_valid())
    #     custom_user = form.save()
    #     self.assertIsNotNone(custom_user.pk)
    #     self.assertEqual(custom_user.username, 'testuser')
    #     self.assertEqual(custom_user.email, 'test@example.com')

    def test_custom_user_form_unique_username(self):
        # Test saving a CustomUser with a duplicate username
        initial_user = CustomUser.objects.create(username='existinguser', email='existing@example.com')
        form_data = {
            'username': 'existinguser',  # Existing username
            'email': 'new@example.com',
            'accessed_objects': [],
        }
        form = CustomUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)


class TestObjectForm(TestCase):

    def test_valid_object_form(self):
        owner = CustomUser.objects.create(username='owner', email='owner@example.com')
        form_data = {
            'file_name': 'example.txt',
            'size': 1024,
            'type': 'txt',
            'owner': owner.pk,
        }
        form = ObjectForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_object_form(self):
        form_data = {
            'file_name': '',  # Empty file_name should raise validation error
            'size': 'not_a_number',  # Non-numeric value for size
            'type': 'txt',  # Example type value
            'owner': None,  # Missing owner should raise validation error
        }
        form = ObjectForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('file_name', form.errors)
        self.assertIn('size', form.errors)
        self.assertIn('owner', form.errors)

    def test_object_form_save(self):
        owner = CustomUser.objects.create(username='owner', email='owner@example.com')
        form_data = {
            'file_name': 'example.txt',
            'size': 1024,
            'type': 'txt',
            'owner': owner.pk,
        }
        form = ObjectForm(data=form_data)
        self.assertTrue(form.is_valid())
        obj = form.save()
        self.assertIsNotNone(obj.id)
        self.assertEqual(obj.file_name, 'example.txt')
        self.assertEqual(obj.size, 1024)
        self.assertEqual(obj.type, 'txt')
        self.assertEqual(obj.owner, owner)

    def test_object_form_generate_id(self):
        owner = CustomUser.objects.create(username='owner', email='owner@example.com')
        form_data = {
            'file_name': 'example.txt',
            'size': 1024,
            'type': 'txt',
            'owner': owner.pk,
        }
        form = ObjectForm(data=form_data)
        self.assertTrue(form.is_valid())
        obj = form.save()
        self.assertTrue(uuid.UUID(obj.id.split('.')[0], version=4))  # Check if ID is a valid UUID

    def test_object_form_date_and_time_auto_add(self):
        owner = CustomUser.objects.create(username='owner', email='owner@example.com')
        form_data = {
            'file_name': 'example.txt',
            'size': 1024,
            'type': 'txt',
            'owner': owner.pk,
        }
        form = ObjectForm(data=form_data)
        self.assertTrue(form.is_valid())
        obj = form.save()
        self.assertIsNotNone(obj.date_and_time)