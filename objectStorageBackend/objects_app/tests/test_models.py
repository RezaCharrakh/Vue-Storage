from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Object, CustomUser

# CustomUser = get_user_model()


class CustomUserModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(
            username='testuser',
            email='testuser@example.com'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertEqual(str(self.user), 'testuser')

    def test_username_uniqueness(self):
        with self.assertRaises(Exception):
            CustomUser.objects.create(username='testuser', email='another@example.com')

    def test_email_uniqueness(self):
        with self.assertRaises(Exception):
            CustomUser.objects.create(username='anotheruser', email='testuser@example.com')


class ObjectModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(
            username='testuser',
            email='testuser@example.com'
        )
        self.object = Object.objects.create(
            file_name='testfile.mp4',
            size=1024,
            type='mp4',
            owner=self.user
        )

    def test_object_creation(self):
        self.assertEqual(self.object.file_name, 'testfile.mp4')
        self.assertEqual(self.object.size, 1024)
        self.assertEqual(self.object.type, 'mp4')
        self.assertEqual(self.object.owner, self.user)
        self.assertTrue(self.object.id.endswith('.mp4'))
        self.assertEqual(str(self.object), 'testfile.mp4')

    def test_object_uuid_generation(self):
        self.assertIsNotNone(self.object.id)
        self.assertIn('.', self.object.id)
        uuid_part, type_part = self.object.id.split('.')
        self.assertEqual(type_part, 'mp4')

    def test_object_owner_relationship(self):
        new_user = CustomUser.objects.create(
            username='newuser',
            email='newuser@example.com'
        )
        obj = Object.objects.create(
            file_name='anotherfile.mp3',
            size=2048,
            type='mp3',
            owner=new_user
        )
        self.assertEqual(obj.owner, new_user)

    def test_object_many_to_many_relationship(self):
        another_object = Object.objects.create(
            file_name='anotherfile.mp4',
            size=2048,
            type='mp4',
            owner=self.user
        )
        self.user.accessed_objects.add(self.object, another_object)
        self.assertIn(self.object, self.user.accessed_objects.all())
        self.assertIn(another_object, self.user.accessed_objects.all())
        self.assertIn(self.user, self.object.accessors.all())
        self.assertIn(self.user, another_object.accessors.all())

    def test_size_field_constraints(self):
        obj = Object.objects.create(
            file_name='testfile2.mp4',
            size=9999999999,  # Assuming there's no size limit set in the model
            type='mp4',
            owner=self.user
        )
        self.assertEqual(obj.size, 9999999999)