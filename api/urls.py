from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register('branch', BranchViewSet, basename='store')
router.register('staff', StaffViewSet, basename='staff')
router.register('customer', CustomerViewSet, basename='customer')
router.register('col_type', CollateralTypeViewSet, basename='col_type')
router.register('collateral', CollateralViewSet, basename='collateral')
router.register('limit', LimitViewSet, basename='limit')

urlpatterns = router.urls
