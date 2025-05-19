from django.urls import path
from .views import SignupView, LoginView, UserInfoView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', UserInfoView.as_view(), name='user-info'),
]
