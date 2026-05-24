from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='expense_categories'
    )
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES
    )
    created_at = models.DateTimeField(auto_created=True)
    
    
    class Meta:
        unique_together = ['user', 'name', 'type']
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return f'{self.name} ({self.type})'


class Transaction(models.Model):
    TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='transactions'
    )
    title = models.CharField(max_length=255)
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES
    )
    date = models.DateField()
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', 'created_at']
        
        def __str__(self):
            return f'{self.title} - {self.amount}'