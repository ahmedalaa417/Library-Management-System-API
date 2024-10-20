from django.contrib import admin
from .models import Book, User, Transaction, OverdueTracking
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'published_date', 'total_copies', 'available_copies')
    search_fields = ('title', 'author', 'isbn')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_membership', 'role', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('role', 'is_active')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'checkout_date', 'return_date')
    list_filter = ('checkout_date', 'return_date')
    search_fields = ('user__username', 'book__title')

@admin.register(OverdueTracking)
class OverdueTrackingAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'overdue_days', 'penalty_amount')
    search_fields = ('transaction__user__username', 'transaction__book__title')