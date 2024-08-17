from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from objects_app.models import Object, CustomUser
from django.conf import settings

# CustomUser = get_user_model()


class CustomUserViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create(
            username='testuser',
            email='test@example.com'
            # password='password123'
        )
        settings.LOGGED_IN_USER = self.user

    def test_upload_file_view(self):
        url = reverse('upload-file')
        file = SimpleUploadedFile("file.mp4", b"file_content", content_type="video/mp4")
        data = {
            'username': 'testuser',
            'file': file
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Object.objects.filter(file_name="file.mp4").exists())

    def test_download_file_view(self):
        obj = Object.objects.create(
            file_name='testfile.mp4',
            size=1024,
            type='mp4',
            owner=self.user
        )

        url = reverse('download-file')
        response = self.client.get(url, {'object_id': obj.id})

        self.assertEqual(response.status_code, 200)
        self.assertIn('download_link', response.json())

    def test_objects_list_view(self):
        obj = Object.objects.create(
            file_name='testfile.mp4',
            size=1024,
            type='mp4',
            owner=self.user
        )

        url = reverse('objects-list')
        response = self.client.get(url, {'username': 'testuser'})

        self.assertEqual(response.status_code, 200)
        self.assertIn('list_of_objects', response.json())
        self.assertGreater(len(response.json()['list_of_objects']), 0)

    def test_delete_file_view(self):
        obj = Object.objects.create(
            file_name='testfile.mp4',
            size=1024,
            type='mp4',
            owner=self.user
        )

        url = reverse('delete-file')
        data = {
            'object_id': obj.id
        }
        response = self.client.post(url, data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())
        self.assertFalse(Object.objects.filter(id=obj.id).exists())

    def test_share_file_view(self):
        obj = Object.objects.create(
            file_name='testfile.mp4',
            size=1024,
            type='mp4',
            owner=self.user
        )

        other_user = CustomUser.objects.create(username='otheruser', email='other@example.com')

        url = reverse('share-file')
        data = {
            'object_id': obj.id
        }
        response = self.client.post(url, data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())
        self.assertIn('combined_users', response.json())

    def test_update_access_view(self):
        obj = Object.objects.create(
            file_name='testfile.mp4',
            size=1024,
            type='mp4',
            owner=self.user
        )

        other_user = CustomUser.objects.create(username='otheruser', email='other@example.com')

        url = reverse('update-access')
        data = {
            'object_id': obj.id,
            'usernames_with_access': ['otheruser'],
            'usernames_without_access': []
        }
        response = self.client.post(url, data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())
        self.assertTrue(other_user.accessed_objects.filter(id=obj.id).exists())
