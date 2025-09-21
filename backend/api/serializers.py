from rest_framework import serializers

from .models import ChatHistory, Document, User


class ChatHistorySerializer(serializers.ModelSerializer):
    documents = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = ChatHistory
        fields = ['id', 'user', 'name', 'created_at', 'modified_at', 'messages', 'documents']
        read_only_fields = ['user', 'created_at', 'messages', 'modified_at', 'documents']

    def save(self, **kwargs):
        kwargs['user'] = self.context['request'].user
        return super().save(**kwargs)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'user', 'chathistory', 'name', 'file', 'doc_type', 'uploaded_at']
        read_only_fields = ['user', 'doc_type', 'uploaded_at', "name"]

    def save(self, **kwargs):
        kwargs['user'] = self.context['request'].user
        return super().save(**kwargs)
    

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'fullname', 'password', 'date_joined']
        read_only_fields = ['id', 'date_joined']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            fullname=validated_data['fullname'],
            password=validated_data['password']
        )
        return user