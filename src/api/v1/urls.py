from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .user.views import CurrentUserView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("users/me/", CurrentUserView.as_view(), name="current_user"),
    # crm
    path("crm/users/", include("api.v1.crm.urls")),
]
