from django.contrib import admin
from .models import UserProfile, BetMatch, Bet, Transaction

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    search_fields = ('user__username',)

@admin.register(BetMatch)
class BetMatchAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'home_odds', 'away_odds', 'draw_odds', 'is_active')
    list_filter = ('is_active',)

@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    list_display = ('user', 'match', 'bet_type', 'amount', 'odds', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'bet_type')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'tx_type', 'created_at')
    list_filter = ('tx_type', 'created_at')
    search_fields = ('user__username',)

