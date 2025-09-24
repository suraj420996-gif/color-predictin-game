from django.db import models
from django.contrib.auth.models import User


class GameResult(models.Model):
    COLOR_CHOICES = [('Red', 'Red'), ('Green', 'Green'), ('Violet', 'Violet')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chosen_color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    result_color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    win = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
class Bet(models.Model):
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('green', 'Green'),
        ('violet', 'Violet'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    result = models.BooleanField(null=True, blank=True)  # Win = True, Loss = False

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} bet {self.amount} on {self.color}"

