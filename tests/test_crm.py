# -*- coding: utf-8 -*-

# zato-testing
from zato_testing import ServiceTestCase

# Our code
from demo.services.crm import GetCustomer

class TestGetCustomer(ServiceTestCase):

    def test_returns_customer_details(self):

        name = 'Alice Johnson'
        email = 'alice@example.com'
        customer_id = 'CUST-001'

        # Prepare test data ..
        self.set_response('crm.api', {
            'name': name,
            'email': email,
        })

        # .. invoke our service ..
        service = self.invoke(GetCustomer, {'customer_id': customer_id})

        # .. and run our assertions.
        self.assertEqual(service.response.payload.name, name)
        self.assertEqual(service.response.payload.email, email)
