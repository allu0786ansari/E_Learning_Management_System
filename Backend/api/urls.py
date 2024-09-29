from api import views as api_view
from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('user/token/', api_view.MyTokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),
    path('user/register/',api_view.RegisterView.as_view()),

]