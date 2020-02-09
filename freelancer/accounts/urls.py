from .views import ForgotPasswordViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'forgotpassword', ForgotPasswordViewSet, 'forgotpassword')
