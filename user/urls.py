from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CustomUserView, ProfileView

router = DefaultRouter()

router.register('user', CustomUserView)
router.register('user-profile', ProfileView)

urlpatterns = [
    path('', include(router.urls))
]