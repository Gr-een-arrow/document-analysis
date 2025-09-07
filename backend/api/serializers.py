from rest_framework import serializers

from .models import ChatHistory


class ChatHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatHistory
        fields = ['id', 'user', 'document', 'name', 'created_at', 'modified_at', 'messages']
        read_only_fields = ['user', 'created_at', 'messages', 'modified_at', 'document']


    # Save function to set the user automatically
    def save(self, **kwargs):
        kwargs['user'] = self.context['request'].user
        return super().save(**kwargs)
    
    # save only the name field on update
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance