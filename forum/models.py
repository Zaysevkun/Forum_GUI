import uuid
from django.db import models


# Create your models here.

class Categories(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', blank=True, on_delete=models.DO_NOTHING)


class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)


class Messages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=255)
    categories = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    posted_at = models.DateTimeField()
    author = models.ForeignKey(Users, on_delete=models.DO_NOTHING)


