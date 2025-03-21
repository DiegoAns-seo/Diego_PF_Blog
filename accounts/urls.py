from django.urls import path
from .views import register_view, login_view, logout_view, profile_view, ProfileUpdateView, PasswordChange

app_name = 'accounts'
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('password_change/', PasswordChange.as_view(), name='password_change'),
]