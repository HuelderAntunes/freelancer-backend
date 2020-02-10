from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'avaliationfields', AvaliationFieldViewSet, 'avaliation')
router.register(r'avaliations', AvaliationViewSet, 'avaliation')
router.register(r'avaliationvalues', AvaliationValueViewSet, 'avaliation')
