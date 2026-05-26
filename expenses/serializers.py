from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Category, Transaction

class RegiserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
    
class CategorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Category
        fields = ['id', 'user', 'name', 'type', 'created_at',]
        read_only_fields = ['id', 'user', 'created_at']
        
        
class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Transaction
        fields = [
            'id',
            'user',
            'category',
            'category_name',
            'title',
            'amount',
            'type',
            'date',
            'note',
            'created_at',
            'updated_at',
            ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
    
    def validate(self, data):
        category = data.get('category')
        transaction_type = data.get('type')
        
        if category and transaction_type and category.type != transaction_type:
            raise serializers.ValidationError({
                'category': 'Category type must match transaction type'
            })
        return data
    
    