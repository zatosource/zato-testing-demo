# -*- coding: utf-8 -*-

from zato_testing import ServiceTestCase

from demo.services.crm import GetCustomer

class TestGetCustomer(ServiceTestCase):

    def test_returns_customer_details(self):

        self.set_response('crm.api', {
            'name': 'Alice Johnson',
            'email': 'alice@acme.com',
        })

        service = self.invoke(GetCustomer, {'customer_id': 'CUST-001'})

        self.assertEqual(service.response.payload.name, 'Alice Johnson')
        self.assertEqual(service.response.payload.email, 'alice@acme.com')
