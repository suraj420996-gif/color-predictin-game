from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)  # default ₹100 balance

    def __str__(self):
        return f"{self.user.username} - Balance: {self.balance}"
