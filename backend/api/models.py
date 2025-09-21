from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, fullname, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')

        if not fullname:
            raise ValueError('Full name is required')

        email = self.normalize_email(email)
        user: User = self.model(email=email, fullname=fullname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, fullname, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    def __str__(self):
        return self.email

class ChatHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_histories")
    name = models.CharField(max_length=255, default="New Chat")
    messages = models.JSONField(default=list)  # List of message dicts with 'role' and 'content'
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ChatHistory {self.id} for {self.user.email}"


class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="documents")
    chathistory = models.ForeignKey(ChatHistory, on_delete=models.CASCADE, related_name="documents", null=True, blank=True)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="documents/")
    doc_type = models.CharField(max_length=20)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Set doc_type based on file extension
        if self.file:
            ext = self.file.name.split('.')[-1].lower()
            if ext in ['txt']:
                self.doc_type = 'txt'
            elif ext in ['docx']:
                self.doc_type = 'docx'
            elif ext in ['pdf']:
                self.doc_type = 'pdf'
            elif ext in ['xlsx', 'xls']:
                self.doc_type = 'excel'
            else:
                self.doc_type = 'unknown'

            self.name = self.file.name.split('.')[0]  # Set name without extension

        return super().save(*args, **kwargs)