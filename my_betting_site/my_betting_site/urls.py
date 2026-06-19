from django.contrib import admin
from django.urls import path
from betting import views

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blackjack/', views.blackjack, name='blackjack'),
    path('blackjack/play/', views.blackjack_play, name='blackjack_play'),
    path('roulette/', views.roulette, name='roulette'),
    path('roulette/spin/', views.roulette_spin, name='roulette_spin'),
    path('casino-admin/', views.casino_admin, name='casino_admin'),
    path('cashier/', views.cashier, name='cashier'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

