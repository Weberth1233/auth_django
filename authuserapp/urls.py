from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
#Criando rotas de listagem, cadastro e pesquisa e etc para tasks
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/register/', CustomRegisterView.as_view(), name='register'),
      # Rota para login que retorna o JWT (access e refresh tokens)
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Rota para refresh do token de acesso usando o refresh token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    path('', include(router.urls)),
]