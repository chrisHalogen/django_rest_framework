from django.urls import path
from .views import LoginView,RegisterView,RefreshView,GetSecuredInfo, TestException

urlpatterns = [
    path('login',LoginView.as_view()),
    path('register',RegisterView.as_view()),
    path('refresh',RefreshView.as_view()),
    path('secured-info',GetSecuredInfo.as_view()),
    path('test-except',TestException.as_view())
]