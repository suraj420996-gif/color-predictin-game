from decimal import Decimal
import random
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Wallet
from .models import Bet

@login_required
def play_game(request):
    wallet = Wallet.objects.get(user=request.user)
    error = None
    success = None
    winning_color = None
    win = None

    if request.method == "POST":
        action = request.POST.get("action")

        # Add Balance
        if action == "add":
            amount = Decimal(request.POST.get("add_amount", 0))
            if amount <= 0:
                error = "Enter a valid amount to add!"
            else:
                wallet.balance += amount
                wallet.save()
                success = f"₹{amount} added successfully!"

        # Withdraw
        elif action == "withdraw":
            amount = Decimal(request.POST.get("withdraw_amount", 0))
            if amount <= 0:
                error = "Enter a valid amount to withdraw!"
            elif amount > wallet.balance:
                error = "Insufficient balance!"
            else:
                wallet.balance -= amount
                wallet.save()
                success = f"₹{amount} withdrawn successfully!"

        # Place Bet
        elif action == "bet":
            color = request.POST.get("color")
            amount = Decimal(request.POST.get("bet_amount", 0))
            if amount <= 0:
                error = "Enter a valid bet amount!"
            elif amount > wallet.balance:
                error = "Insufficient balance for this bet!"
            else:
                # Deduct bet
                wallet.balance -= amount
                wallet.save()

                # Random result
                winning_color = random.choice(["red", "green", "violet"])
                win = (color == winning_color)

                if win:
                    payout = amount * Decimal(2)
                    wallet.balance += payout
                    wallet.save()

                # Save bet
                Bet.objects.create(user=request.user, color=color, amount=amount, result=win)
                success = f"Bet placed on {color.title()} for ₹{amount}"

    return render(request, "game/play.html", {
        "wallet": wallet,
        "error": error,
        "success": success,
        "winning_color": winning_color,
        "win": win,
    })
