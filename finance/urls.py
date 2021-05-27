from rest_framework import routers, serializers, viewsets
from .views import UserViewSet, InvoiceViewSet, InvoiceCustomerUpdateSet
from django.urls import path, include

app_name = 'finance'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'updates', InvoiceCustomerUpdateSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls,)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'),)
]