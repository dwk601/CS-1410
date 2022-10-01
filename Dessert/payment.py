from enum import Enum


class PayType(Enum):
    CASH = 1
    CARD = 2
    PHONE = 3


class Payment():
    def __init__(self, pay_type):
        self.pay_type = pay_type

    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value

    def __str__(self):
        return "{}".format(self.pay_type.name)

    def __repr__(self):
        return "{}".format(self.pay_type.name)

    def get_payment_type(self):
        return self.pay_type.name

    def get_payment_amount(self):
        return self.pay_type.value
