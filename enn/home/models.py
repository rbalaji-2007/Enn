from django.db import models

class UserSettings(models.Model):
    name = models.CharField(max_length=100, default="Vedant")
    currency = models.CharField(max_length=10, default="₹")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User Settings: {self.name}"

    @classmethod
    def get_settings(cls):
        settings, _ = cls.objects.get_or_create(id=1, defaults={"name": "Vedant", "currency": "₹"})
        return settings

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ("EXPENSE", "Expense"),
        ("CREDIT", "Credit"),
    )

    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES, default="EXPENSE")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=255, blank=True, default="")
    category = models.CharField(max_length=50)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"[{self.transaction_type}] {self.category} - {self.amount} ({self.date})"
