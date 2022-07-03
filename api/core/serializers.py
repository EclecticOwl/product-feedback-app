from dataclasses import fields
from rest_framework import serializers
from .models import Product, Feedback, CustomUser


class ProductUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'username']


class ProductSerializer(serializers.ModelSerializer):
    product_owner = ProductUserSerializer(source='owner', read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'owner', 'product_owner']
        read_only_fields = ['owner']

      
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = [
            'id',
            'product_name',
            'feedback_owner',
            'title',
            'category',
            'upvotes',
            'status',
            'description',
            ]
