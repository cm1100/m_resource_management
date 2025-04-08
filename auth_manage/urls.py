from .views import ObtainUserTokenPairView,RefreshUserTokenView
from django.urls import path

urlpatterns = [
    path('token/', ObtainUserTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', RefreshUserTokenView.as_view(), name='token_refresh'),
]
