from django.urls import path
from .views import SignupUser, loginUser, resetpassword, signout

urlpatterns = [
    path('signup/',SignupUser, name='signup' ),
    path('',loginUser, name='login' ),
    path('reset/password/',resetpassword, name='reset' ),
    path('home/logout',signout, name='logout' ),
]