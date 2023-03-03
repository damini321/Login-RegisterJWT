from django.urls import path, include
#from .views import UserRegistrationView, UserLoginView,UserChangePasswordView,SendPasswordResetEmailView, UserPasswordResetView, UserDataListCreateView, UserDataRetrieveUpdateDestroyView
from register.views import *
urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('sendresetpasswordemail/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('userdata/', UserDataListCreateView.as_view()),
    path('userdata/<int:pk>/', UserDataRetrieveUpdateDestroyView.as_view()),
  

]