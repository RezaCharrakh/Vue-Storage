from django.urls import path
from .views import (upload_file_view, download_file_view, objects_list_view, delete_file_view
                    , share_file_view, update_access_view)

urlpatterns = [
    path('upload_file', upload_file_view, name='upload-file'),
    path('download_file', download_file_view, name='download-file'),
    path('objects_list', objects_list_view, name='objects-list'),
    path('delete_file', delete_file_view, name='delete-file'),
    path('share_file', share_file_view, name='share-file'),
    path('update_access', update_access_view, name='update-access'),
]
