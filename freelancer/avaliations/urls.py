from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'avaliationfields',
                AvaliationFieldViewSet, 'avaliationfields')
router.register(r'avaliations', AvaliationViewSet, 'avaliations')
router.register(r'avaliationvalues',
                AvaliationValueViewSet, 'avaliationvalues')
