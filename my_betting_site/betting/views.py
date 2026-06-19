from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import UserProfile, Transaction
import json
import random

@login_required(login_url='login')
def home(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'betting/home.html', {'balance': profile.balance})

@login_required(login_url='login')
def blackjack(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'betting/blackjack.html', {'balance': profile.balance})

@login_required(login_url='login')
def roulette(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'betting/roulette.html', {'balance': profile.balance})

@login_required(login_url='login')
def roulette_spin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        bet_amount = int(data.get('bet', 0))
        bet_type = data.get('type') # 'red', 'black', 'number'
        bet_value = data.get('value') # אם זה מספר, נקבל למשל '14'
        
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        
        if profile.balance < bet_amount or bet_amount <= 0:
            return JsonResponse({'status': 'error', 'message': 'Insufficient funds!'})
            
        # הורדת סכום ההימור מהארנק
        profile.balance -= bet_amount
        profile.save()
        
        # הגרלת מספר הרולטה (0-36)
        winning_number = random.randint(0, 36)
        
        # הגדרת הצבעים ברולטה תקנית
        red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        if winning_number == 0:
            winning_color = 'green'
        elif winning_number in red_numbers:
            winning_color = 'red'
        else:
            winning_color = 'black'
            
        # בדיקת זכייה
        won = False
        payout = 0
        
        if bet_type == 'red' and winning_color == 'red':
            won = True
            payout = bet_amount * 2
        elif bet_type == 'black' and winning_color == 'black':
            won = True
            payout = bet_amount * 2
        elif bet_type == 'number' and str(winning_number) == str(bet_value):
            won = True
            payout = bet_amount * 36
            
        if won:
            profile.balance += payout
            profile.save()
            
        return JsonResponse({
            'status': 'success',
            'winning_number': winning_number,
            'winning_color': winning_color,
            'won': won,
            'payout': payout,
            'new_balance': profile.balance
        })
        
    return JsonResponse({'status': 'error', 'message': 'Invalid Request'})

@login_required(login_url='login')
def cashier(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    error_msg = None
    success_msg = None

    if request.method == 'POST':
        tx_type = request.POST.get('tx_type')
        amount = int(request.POST.get('amount', 0))

        if amount <= 0:
            error_msg = "Please enter a valid amount."
        elif tx_type == 'withdrawal' and profile.balance < amount:
            error_msg = "Insufficient funds for withdrawal."
        else:
            Transaction.objects.create(user=request.user, amount=amount, tx_type=tx_type, status='pending')
            success_msg = f"Your {tx_type} request for ₪{amount} has been submitted for admin approval."

    history = Transaction.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'betting/cashier.html', {'balance': profile.balance, 'error_msg': error_msg, 'success_msg': success_msg, 'history': history})

@user_passes_test(lambda u: u.is_superuser, login_url='login')
def casino_admin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        action = data.get('action')
        tx_id = data.get('tx_id')

        try:
            tx = Transaction.objects.get(id=tx_id)
            if tx.status == 'pending':
                profile, created = UserProfile.objects.get_or_create(user=tx.user)
                if action == 'approve':
                    tx.status = 'approved'
                    if tx.tx_type == 'deposit':
                        profile.balance += tx.amount
                    elif tx.tx_type == 'withdrawal':
                        profile.balance -= tx.amount
                    profile.save()
                elif action == 'reject':
                    tx.status = 'rejected'
                tx.save()
                return JsonResponse({'status': 'success', 'message': f'Transaction {action}d successfully.'})
        except Transaction.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Transaction not found.'})

    pending_txs = Transaction.objects.filter(status='pending').select_related('user')
    users = User.objects.all().select_related('profile')
    return render(request, 'betting/admin_panel.html', {'users': users, 'pending_txs': pending_txs})

def register_view(request):
    error_msg = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.get_or_create(user=user)
            login(request, user)
            return redirect('home')
        else:
            error_msg = " ".join([f"{k}: {v[0]}" for k, v in form.errors.items()])
    else:
        form = UserCreationForm()
    return render(request, 'betting/register.html', {'form': form, 'error_msg': error_msg})

def login_view(request):
    error_msg = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            error_msg = "Invalid username or password."
    else:
        form = AuthenticationForm()
    return render(request, 'betting/login.html', {'form': form, 'error_msg': error_msg})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def blackjack_play(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        action = data.get('action')
        bet = int(data.get('bet', 0))
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        
        if action == 'start' or action == 'double':
            if profile.balance >= bet:
                profile.balance -= bet
                profile.save()
                return JsonResponse({'status': 'success', 'new_balance': profile.balance})
            return JsonResponse({'status': 'error', 'message': 'Insufficient funds!'})
        elif action == 'end':
            profile.balance += bet
            profile.save()
            return JsonResponse({'status': 'success', 'new_balance': profile.balance})
    return JsonResponse({'status': 'error', 'message': 'Invalid Request'})

