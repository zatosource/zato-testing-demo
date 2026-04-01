# -*- coding: utf-8 -*-

from zato.server.service import Service

class GetCustomer(Service):
    """ Returns customer details from the CRM system.
    """
    name = 'crm.customer.get'

    input = 'customer_id'
    output = 'name', 'email'

    def handle(self):

        conn = self.out.rest['crm.api'].conn
        response = conn.get(self.cid, params={'id': self.request.input.customer_id})

        self.response.payload.name = response.data['name']
        self.response.payload.email = response.data['email']
