from django.test import TestCase

# Create your tests here.

from .models import Invoice
from django.contrib.auth.models import User


class EntryModelTest(TestCase):

    # def test_string_representation(self):
    #     self.fail("TODO Test incomplete")

    def test_string_representation(self):
        """ Testing on django model __str__ for object is equal or not """
        user = User(username='user-1',
                    email='emailid@gmail.com',
                    first_name='user123')

        invoice = Invoice(customer=user,
                          project_name='p1',
                          amount=15000,
                          )

        self.assertEqual(str(invoice), "{0}-{1}".format(invoice.customer, invoice.amount))

