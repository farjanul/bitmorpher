from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.users.api.v1.views import (
    CustomUserViewSet,
)

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r'users', CustomUserViewSet)

app_name = "api"

urlpatterns = [

]

urlpatterns += router.urls
