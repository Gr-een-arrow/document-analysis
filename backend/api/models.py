from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()  


class ChatHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_histories")
    name = models.CharField(max_length=255, default="New Chat")
    messages = models.JSONField(default=list)  # List of message dicts with 'role' and 'content'
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ChatHistory {self.id} for {self.user.username}"


class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="documents")
    chathistory = models.ForeignKey(ChatHistory, on_delete=models.CASCADE, related_name="documents", null=True, blank=True)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="documents/")
    doc_type = models.CharField(max_length=20)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(blank=True, null=True)

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

        return super().save(*args, **kwargs)