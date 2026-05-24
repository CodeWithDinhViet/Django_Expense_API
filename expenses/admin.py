from django.contrib import admin
from .models import Category, Transaction
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'user', 'created_at')
    list_filter = ('type', 'created_at')
    search_fields = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'amount', 'type', 'category', 'user', 'date')
    list_filter = ('type', 'category', 'date')
    search_fields = ('title', 'note')