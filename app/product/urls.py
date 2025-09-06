from django.urls import include, path
from .views import CartModelViewSet, CategoryModelViewSet, OrderItemModelViewSet, OrderModelViewSet, ProductModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"products", ProductModelViewSet)
router.register(r"categories", CategoryModelViewSet)
router.register(r"order-items", OrderItemModelViewSet)
router.register(r"orders", OrderModelViewSet)
router.register(r"carts", CartModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

