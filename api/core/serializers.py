from rest_framework import serializers
from .models import Product, Feedback


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['owner', 'title']


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


    