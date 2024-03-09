# example/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    # path('home/', views.home),
    path('login/', views.login),
    path('post/', views.post),
    path('redeem/', views.redeem),
    path('leaderboard/', views.leaderboard),
    path('feed/', views.feed),
]