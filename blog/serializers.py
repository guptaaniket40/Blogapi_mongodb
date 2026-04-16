from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()
    author = serializers.CharField(max_length=100)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        blog = Blog(**validated_data)
        blog.save()
        return blog

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance