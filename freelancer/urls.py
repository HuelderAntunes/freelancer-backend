from django.contrib import admin
from django.urls import path, include
from freelancer.accounts.urls import router as accounts_router
from freelancer.avaliations.urls import router as avaliations_router
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(avaliations_router.urls)),
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
