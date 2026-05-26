from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RegisterView, CategoryViewSet, TransactionViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')

router.register('transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]