from django.urls import path
from .views import UserSignUpView, UserUpdateView, profile

app_name = 'accounts'

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='user_signup'),
    path('profile/', profile, name='user_profile'),
    path('profile/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
]
