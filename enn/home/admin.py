from django.contrib import admin
# pyrefly: ignore [missing-import]
from .models import Transaction, UserSettings

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "transaction_type", "category", "amount", "date", "description")
    list_filter = ("transaction_type", "category", "date")
    search_fields = ("category", "description")

@admin.register(UserSettings)
class UserSettingsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "currency")
