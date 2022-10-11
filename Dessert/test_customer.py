import pytest 
from dessertshop import Customer
from dessert import *

#test Customer class
class TestCustomer(object):
    def test_init(self):
        customer = Customer("Bob")
        assert customer.customer_name == "Bob"
        assert customer.order_history == []
        assert customer.customer_id == 0

    def test_add2history(self):
        customer = Customer("Bob")
        customer.add2history("cookie")
        assert customer.order_history == ["cookie"]
        
    def test_add_order_history(self):
        customer = Customer("Bob")
        customer.add_order_history("cookie")
        assert customer.order_history == ["cookie"]
        
    def test_customer_db(self):
        customer = Customer("Bob")
        customer_db = {}
        customer_db[customer.customer_name] = customer
        assert customer_db == {"Bob": customer}
        
    def test_get_customer_name(self):
        customer = Customer("Bob")
        assert customer.get_customer_name() == "Bob"
        
        
if __name__ == "__main__":
    pytest.main()