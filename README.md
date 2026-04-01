# Zato Testing Demo

This project demonstrates how to test Zato services using the [zato-testing](https://pypi.org/project/zato-testing/) framework.

## Quick Start

```bash
git clone https://github.com/zatosource/zato-testing-demo.git
cd zato-testing-demo
make test
```

## What's Inside

A sample service that calls an external CRM API:

```python
class GetCustomer(Service):
    name = 'crm.customer.get'

    input = 'customer_id'
    output = 'name', 'email'

    def handle(self):
        conn = self.out.rest['crm.api'].conn
        response = conn.get(self.cid, params={'id': self.request.input.customer_id})

        self.response.payload.name = response.data['name']
        self.response.payload.email = response.data['email']
```

And a test that simulates the API response:

```python
class TestGetCustomer(ServiceTestCase):

    def test_returns_customer_details(self):

        self.set_response('crm.api', {
            'name': 'Alice Johnson',
            'email': 'alice@acme.com',
        })

        service = self.invoke(GetCustomer, {'customer_id': 'CUST-001'})

        self.assertEqual(service.response.payload.name, 'Alice Johnson')
        self.assertEqual(service.response.payload.email, 'alice@acme.com')
```

## Learn More

- [Zato Testing Documentation](https://zato.io/en/docs/4.1/api-testing/index.html)
- [Zato Homepage](https://zato.io)
