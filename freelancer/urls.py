from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from freelancer.accounts.views import *
from freelancer.avaliations.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()

# Accounts
router.register(r'forgotpassword', ForgotPasswordViewSet, 'forgotpassword')
router.register(r'users', UserViewSet, 'users')
router.register(r'users/personaldata', PersonalDataViewSet)
router.register(r'users/bankaccount', BankAccountViewSet)
router.register(r'groups', GroupViewSet, 'groups')

# Avaliations
router.register(r'avaliations', AvaliationViewSet, 'avaliations')
router.register(r'avaliation/values',
                AvaliationValueViewSet, 'avaliationvalues')
router.register(r'avaliation/fields',
                AvaliationFieldViewSet, 'avaliationfields')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
