from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.


class Invoice(models.Model):
    """
        Invoice model for customers to make a payment

    """
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          )
    customer = models.ForeignKey(User,
                                 on_delete=models.PROTECT,
                                 help_text='Customer',
                                 )
    project_name = models.CharField(max_length=100,
                                    help_text='Please specify project name',
                                    )

    amount = models.FloatField(help_text='Please specify amount',
                               )
    status = models.BooleanField(default=False,
                                 help_text='Check for invoice'
                                 )
    created_on = models.DateTimeField(auto_now_add=True)
    paid_on = models.DateTimeField(blank=True,
                                   null=True,
                                   )
    paid_status = models.BooleanField(default=False)

    def __str__(self):
        return '{0}-{1}'.format(self.customer, self.amount)




