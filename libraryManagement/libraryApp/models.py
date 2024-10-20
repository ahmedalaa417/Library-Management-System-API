from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)  # ISBN is unique
    published_date = models.DateField()
    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"

class User(AbstractUser):
    email = models.EmailField(unique=True)  
    date_of_membership = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('member', 'Member'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member') 
    

    def __str__(self):
        return self.username


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='transactions')
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()  # Set when returned

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"
    

class OverdueTracking(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    overdue_days = models.PositiveIntegerField(default=0)
    penalty_amount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def calculate_penalty(self):
        # Calculate overdue days and penalty amount
        self.overdue_days = (timezone.now().date() - self.transaction.checkout_date.date()).days
        if self.overdue_days > 0:
            self.penalty_amount = self.overdue_days * 2.00  # $2.00 per day penalty
        self.save()

    def __str__(self):
        return f"Overdue {self.overdue_days} days - Penalty: {self.penalty_amount}"