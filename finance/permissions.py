# coding=utf-8
from rest_framework import permissions
from django.contrib.auth.models import User


class IsSuperUser(permissions.BasePermission):
    """ Super user permission """
    message = "Only Super user can access this page"

    def has_permission(self, request, view):
        """ Permission on super user """

        return request.user.is_superuser


class IsCustomerGroup(permissions.BasePermission):
    """ Customer group user permission """
    message = "Only customer group can access this page"

    def has_permission(self, request, view):
        """ Permission on customer user """
        return User.objects.filter(username=request.user, groups__name='customer').exists()
