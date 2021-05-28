from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, InvoiceSerializer, InvoiceCustomerSerializer
from .models import Invoice
from .permissions import IsSuperUser, IsCustomerGroup


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)
    http_method_names = ['get', 'post']


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = (IsSuperUser|IsCustomerGroup,)
    http_method_names = ['get',
                         'post',
                         'put',
                         'patch',
                         ]
    lookup_field = 'id'

    def get_queryset(self):
        qs = super(InvoiceViewSet, self).get_queryset()

        if User.objects.filter(username=self.request.user, groups__name='customer').exists():
            return qs.filter(customer=self.request.user, status=True)
        return qs

    def http_method_not_allowed(self, request, *args, **kwargs):
        h = super(InvoiceViewSet, self).http_method_not_allowed(request, *args, **kwargs)
        if User.objects.filter(username=self.request.user, groups__name='customer').exists():
            return ['patch']
        return h

    def get_serializer_class(self):
        ser = super(InvoiceViewSet, self).get_serializer_class()
        if self.request.user.is_superuser:
            return ser
        return InvoiceCustomerSerializer


#

