from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import StoreViewSet, StaffViewSet

router = SimpleRouter()
router.register('store', StoreViewSet, basename="store")
router.register('staff', StaffViewSet, basename="staff")
urlpatterns = router.urls
