from rest_framework.routers import DefaultRouter
from .views import CartModelViewSet, UserModelViewSet

router = DefaultRouter()

router.register('user', UserModelViewSet)
router.register('cart', CartModelViewSet)

urlpatterns = router.urls