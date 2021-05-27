from django.shortcuts import render

# Create your views here.

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
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
    permission_classes = (IsSuperUser,)
    http_method_names = ['get', 'post']


class InvoiceCustomerUpdateSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()

    serializer_class = InvoiceCustomerSerializer
    permission_classes = (IsCustomerGroup,)
    http_method_names = ['get', 'put']

    # def get_queryset(self):
    #     qs = Invoice.objects.filter(customer=self.request.user)
    #     return qs


