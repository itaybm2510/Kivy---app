from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    balance = models.IntegerField(default=1000)

    def __str__(self):
        return f"{self.user.username} - ₪{self.balance}"

class BetMatch(models.Model):
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    home_odds = models.FloatField()
    away_odds = models.FloatField()
    draw_odds = models.FloatField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"

class Bet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(BetMatch, on_delete=models.CASCADE, null=True, blank=True)
    bet_type = models.CharField(max_length=20) # 'home', 'away', 'draw', 'blackjack'
    amount = models.IntegerField()
    odds = models.FloatField(default=2.0)
    status = models.CharField(max_length=20, default='pending') # 'pending', 'won', 'lost'
    created_at = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    tx_type = models.CharField(max_length=20) # 'deposit', 'withdrawal'
    status = models.CharField(max_length=20, default='pending') # 'pending', 'approved', 'rejected'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.tx_type} - {self.amount} ({self.status})"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()

