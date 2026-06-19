from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blackjack/', views.blackjack, name='blackjack'),
    path('casino-admin/', views.casino_admin, name='casino_admin'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('blackjack/play/', views.blackjack_play, name='blackjack_play'),
]

