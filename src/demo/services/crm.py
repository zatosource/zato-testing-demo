# -*- coding: utf-8 -*-

# Zato
from zato.server.service import Service

class GetCustomer(Service):
    """ Returns customer details from the CRM system.
    """
    name = 'crm.customer.get'

    input = 'customer_id'
    output = 'name', 'email'

    def handle(self):

        # Get the CRM connection ..
        conn_name = 'crm.api'
        conn = self.out.rest[conn_name].conn

        # .. the data to be sent ..
        params = {'id': self.request.input.customer_id}

        # .. invoke the CRM ..
        response = conn.get(self.cid, params)

        # .. and build our response.
        self.response.payload.name = response.data['name']
        self.response.payload.email = response.data['email']