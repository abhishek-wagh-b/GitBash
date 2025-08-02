from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from api.views import RegisterView,LoginView

urlpatterns = [
    path('', include("api.urls")),
    path('register/', RegisterView.as_view(), name="Auth_Register"),
    path('login/', LoginView.as_view(), name="Auth_Login"),
    #path('api/auth/', include("api.urls")),
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', TokenRefreshView.as_view(), name='token_refresh'),
]
