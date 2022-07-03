from dataclasses import fields
from rest_framework import serializers
from .models import Product, Feedback, CustomUser



class ProductSerializer(serializers.ModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')
    first_name = serializers.ReadOnlyField(source='owner.first_name')
    last_name = serializers.ReadOnlyField(source='owner.last_name')

    class Meta:
        model = Product
        fields = ['id', 'title', 'owner', 'first_name', 'last_name']
        read_only_fields = ['owner', 'first_name', 'last_name', 'id']

      
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
