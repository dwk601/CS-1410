import pytest 
from dessertshop import *
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
        
if __name__ == "__main__":
    pytest.main()
    
    print("All tests passed!")