from rest_framework import serializers

from .models import ChatHistory, Document


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
        fields = ['id', 'user', 'chathistory', 'name', 'file', 'doc_type', 'uploaded_at', 'metadata']
        read_only_fields = ['user', 'doc_type', 'uploaded_at']

    def save(self, **kwargs):
        kwargs['user'] = self.context['request'].user
        return super().save(**kwargs)