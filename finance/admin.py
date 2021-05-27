from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .models import Invoice
from django.utils import timezone


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['customer',
                    'amount',
                    'project_name',
                    ]

    def get_queryset(self, request):
        qs = super(InvoiceAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif User.objects.filter(username=request.user, groups__name='customer').exists():
            return qs.filter(customer=request.user)
        else:
            return super(InvoiceAdmin, self).get_queryset(request)

    def save_model(self, request, obj, form, change):
        if User.objects.filter(username=request.user, groups__name='customer').exists():
            obj.paid_on = timezone.now()
            obj.paid_status = True
            obj.save()

        super(InvoiceAdmin, self).save_model(request, obj, form, change)
