import uuid
from django.db import models


class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    accessed_objects = models.ManyToManyField('Object', related_name='accessors')

    def __str__(self):
        return self.username


class Object(models.Model):
    id = models.CharField(primary_key=True, max_length=50, editable=False)
    file_name = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    date_and_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10)  # Example values: 'mp3', 'mp4', etc.
    owner = models.ForeignKey(CustomUser, related_name='owned_objects', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = f"{uuid.uuid4()}.{self.type}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.file_name


