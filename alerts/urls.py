from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlertViewSet, index, create_alert

# AlertSseView, create_alert

router = DefaultRouter()
router.register(r"alerts", AlertViewSet, basename="alert")


urlpatterns = [
    path("api/", include(router.urls)),
    path("index/", index, name="index"),
    path("create_alert/", create_alert, name="create_alert"),
]
