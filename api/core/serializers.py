from rest_framework import serializers
from .models import Product, Feedback, CustomUser



class FeedbackSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    product_name = serializers.ReadOnlyField(source='product_name.title')

    class Meta:
        model = Feedback
        fields = ['id', 'product_name', 'owner', 'title', 'category', 'upvotes', 'status', 'description']
        read_only_fields = ['id', 'owner', 'upvotes']
        depth = 1

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    first_name = serializers.ReadOnlyField(source='owner.first_name')
    last_name = serializers.ReadOnlyField(source='owner.last_name')
    feedback = FeedbackSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'owner', 'first_name', 'last_name', 'feedback']
        read_only_fields = ['owner', 'first_name', 'last_name', 'id', 'feedback']
    
   