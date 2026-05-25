from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Transaction
from .serializers import (
    RegiserSerializer,
    CategorySerializer,
    TransactionSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegiserSerializer
    permission_classes = [AllowAny]
    
    
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Category.objects.all().order_by('-created_at')
        
        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
            
        category_type = self.request.query_params.get('type')
        
        if category_type:
            queryset = queryset.filter(type=category_type)
        
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Transaction.objects.all()
        
        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
            
        transaction_type = self.request.query_params.get('type')
        category = self.request.query_params.get('category')
        date = self.request.query_params('date')
        month = self.request.query_params('month')
        
        if transaction_type:
            queryset = queryset.filter(type=transaction_type)
            
        if category:
            queryset = queryset.filter(category_id=category)
            
        if date:
            queryset = queryset.filter(date=date)
            
        if month:
            queryset = queryset.filter(date__month = month)
            
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
    @action(detail=False, methods=['get'])
    def summary(self, request):
        queryset = self.get_queryset()
        
        total_income = queryset.filter(type='income').aggreate(total=Sum('amount'))['total'] or 0
        
        total_expense = queryset.filter(type='expense').aggreate(total=Sum('amount'))['total'] or 0
        
        balance = total_income - total_expense
        
        data = {
            'total_income': total_income,
            'total_expense': total_expense,
            'balance': balance,
        }
        
        return Response(data)