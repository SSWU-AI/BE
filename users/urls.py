from django.urls import path
from .views import SignupView, LoginView, LogoutView, UserInfoView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', UserInfoView.as_view(), name='user-info'),
]
