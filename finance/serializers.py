from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Invoice
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
                                   max_length=50)
    first_name = serializers.CharField(required=True,
                                       max_length=60)

    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'first_name',
                  ]


class InvoiceSerializer(serializers.ModelSerializer):
    customer = UserSerializer()

    class Meta:
        model = Invoice
        fields = ['id',
                  'project_name',
                  'amount',
                  'status',
                  'customer',
                  # 'paid_status',
                  ]

    def add_cutomer_group(self, user):
        try:
            customer_group = Group.objects.get(name='customer')
            customer_group.user_set.add(user)

            # todo
            # this password is for temp only, strictly remove
            u = User.objects.get(username=user)
            u.set_password('finance123')
            u.save()
        except ObjectDoesNotExist:
            raise ValueError('Customer group not added...')

    def validate(self, attrs):
        email = dict(attrs['customer'])['email']

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email',
                                               'Email ID already existing ... '})

        return super(InvoiceSerializer, self).validate(attrs)

    def create(self, validated_data):
        # print(validated_data)
        c = dict(validated_data.pop('customer'))
        user = User.objects.create_user(**c, is_staff=True)

        # adding user into customer group.
        self.add_cutomer_group(user)
        invoice = Invoice.objects.create(**validated_data, customer=user)
        return invoice


class InvoiceCustomerSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(read_only=True)
    status = serializers.BooleanField(read_only=True)
    amount = serializers.FloatField(read_only=True)

    class Meta:
        model = Invoice
        fields = ['id',
                  'project_name',
                  'amount',
                  'status',
                  'paid_status'
                  ]

    def update(self, instance, validated_data):

        if instance.paid_status:
            instance.paid_status = True
            instance.paid_on = timezone.now()
            instance.save()

        return instance




