import email
import json

from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.views import APIView

from .models import Object, CustomUser
from .serializers import ObjectSerializer, CustomUserSerializer
from django.http import JsonResponse
from django.conf import settings
from objects_app.utils import S3ResourceSingleton, upload_file, objects_list, delete_file
from django.core.paginator import Paginator
from django.db.models import Sum
from django.core.mail import send_mail
from django.conf import settings
from operator import attrgetter


# class ObjectCreateView(generics.CreateAPIView):
#     queryset = Object.objects.all()
#     serializer_class = ObjectSerializer

@csrf_exempt
def upload_file_view(request):
    # Initialize the Singleton with settings
    S3ResourceSingleton()

    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            settings.LOGGED_IN_USER = CustomUser.objects.get(username=username)
            file = request.FILES['file']
            file_name = file.name
            file_size = file.size

            dot_position = file_name.rfind('.')
            if dot_position != -1:
                file_type = file_name[dot_position + 1:]
            else:
                file_type = ''

            object = Object.objects.create(
                file_name=file_name,
                size=file_size,
                type=file_type,
                owner=settings.LOGGED_IN_USER
            )

            success = upload_file(file, object.id)

            if success:
                return JsonResponse({'message': 'File uploaded successfully'}, status=200)
            else:
                return JsonResponse({'message': 'Failed to upload file'}, status=500)
        except UnicodeEncodeError as e:
            print(f"UnicodeEncodeError: {e}")
            return JsonResponse({'message': 'Failed to encode file name'}, status=400)
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'message': 'An error occurred'}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)


@csrf_exempt
def download_file_view(request):
    # Initialize the Singleton with settings
    # S3ResourceSingleton()

    if request.method == 'GET':
        object_id = request.GET.get('object_id')
        # file_name = file["file_name"]
        # object_id = file["object_id"]
        download_link = f"https://object-storage-web-project.s3.ir-thr-at1.arvanstorage.ir/{object_id}"
        print(download_link)
        # file_format = file["type"]
        # download_path = f"D:/All/Git Projects/Object-Storage/CF-Storage/Downloads/{file_name}"

        # success = download_file(download_path, object_id)

        # if success:
        return JsonResponse({'message': 'File downloaded successfully',
                             'download_link': download_link}, status=200)
        # else:
        #     return JsonResponse({'message': 'Failed to download file'}, status=500)

    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)


@csrf_exempt
def objects_list_view(request):
    # Initialize the Singleton with settings
    S3ResourceSingleton()

    if request.method == 'GET':
        total_size = 0

        query = request.GET.get('query', None)
        page_number = request.GET.get('page')
        username = request.GET.get('username')
        settings.LOGGED_IN_USER = CustomUser.objects.get(username=username)

        object_key = objects_list()
        if object_key is not None:

            # Fetch objects owned by the logged-in user
            owned_objects = Object.objects.filter(owner=settings.LOGGED_IN_USER)
            if len(owned_objects) != 0:
                total_size1 = owned_objects.aggregate(total_size=Sum('size'))['total_size']
                total_size += total_size1

            # Fetch objects accessed by the logged-in user
            accessed_objects = CustomUser.objects.get(username=settings.LOGGED_IN_USER).accessed_objects.all()
            if len(accessed_objects) != 0:
                total_size2 = accessed_objects.aggregate(total_size=Sum('size'))['total_size']
                total_size += total_size2

            #  Check if there is a query in search bar or not
            if query:
                owned_objects = owned_objects.filter(file_name__icontains=query)
                accessed_objects = accessed_objects.filter(file_name__icontains=query)

            # Combine both query sets into a single list
            list_of_objects = list(owned_objects) + list(accessed_objects)

            # Sort list_of_objects by date_created attribute
            sorted_objects = sorted(list_of_objects, key=attrgetter('date_and_time'), reverse=True)

            paginator = Paginator(sorted_objects, 24)
            page_objects = paginator.get_page(page_number)

            # Serialize the list of objects
            serialized_objects = ObjectSerializer(page_objects, many=True).data

            return JsonResponse({
                'message': 'List of objects showed successfully',
                'list_of_objects': serialized_objects,
                'total_pages': page_objects.paginator.num_pages,
                'total_size': total_size
            }, status=200)

        else:
            return JsonResponse({'message': 'Failed to show list of objets'}, status=500)
    else:
        return JsonResponse({'error': 'GET method required'}, status=400)


@csrf_exempt
def delete_file_view(request):
    # Initialize the Singleton with settings
    S3ResourceSingleton()

    if request.method == 'POST':
        file = json.loads(request.body)
        object_id = file["object_id"]
        success = delete_file(object_id)

        if success:
            Object.objects.get(id=object_id).delete()
            return JsonResponse({'message': 'File deleted successfully'}, status=200)
        else:
            return JsonResponse({'message': 'Failed to delete file'}, status=500)
    else:
        return JsonResponse({'error': 'POST method required'}, status=400)


@csrf_exempt
def share_file_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        object_id = data["object_id"]


        users_with_access = CustomUser.objects.filter(accessed_objects=object_id)
        all_users = CustomUser.objects.all()

        # Remove users with access from all users
        users_without_access = all_users.difference(users_with_access)

        # Combine both query sets into a single list
        combined_users = list(users_with_access) + list(users_without_access)

        # Serialize the lists of users
        ser_combined_users = CustomUserSerializer(combined_users, many=True).data

        return JsonResponse({
            'message': 'List of users showed successfully',
            'combined_users': ser_combined_users
        }, status=200)

    else:
        return JsonResponse({'error': 'POST method required'}, status=400)


@csrf_exempt
def update_access_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        object_id = data["object_id"]
        usernames_with_access = data.get("usernames_with_access", [])
        usernames_without_access = data.get("usernames_without_access", [])

        # Retrieve the object
        updated_object = get_object_or_404(Object, pk=object_id)

        # Retrieve users
        users_with_access = CustomUser.objects.filter(username__in=usernames_with_access)
        users_without_access = CustomUser.objects.filter(username__in=usernames_without_access)

        # Update access lists
        for user in users_with_access:
            if updated_object not in user.accessed_objects.all():
                print("if")
                user.accessed_objects.add(updated_object)
                user.save()

                # Send an email notification
                send_mail(
                    'Access granted to file',
                    f'Hello {user.username},\n\nYou have been given access to file {updated_object.file_name}.',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                )

        for user in users_without_access:
            user.accessed_objects.remove(updated_object)
            user.save()

        return JsonResponse({'message': 'Access updated successfully.'}, status=200)

    return JsonResponse({'error': 'POST method required'}, status=400)
