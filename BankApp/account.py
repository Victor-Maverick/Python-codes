from BankApp.insufficient_funds_error import InsufficientFundsError
from BankApp.invalid_amount_error import InvalidAmountError
from BankApp.invalid_pin_error import InvalidPinError


class Account:
    def __init__(self, name: str, number: int, pin: str):
        self.pin = pin
        self.balance = 0
        self.number = number

    def deposit(self, amount: int):
        self.validate_amount(amount)
        self.balance += amount

    @staticmethod
    def validate_amount(amount):
        if amount <= 0:
            raise InvalidAmountError('amount should be greater than zero')

    def get_balance(self, pin):
        self.validate_pin(pin)
        return self.balance

    def validate_pin(self, pin):
        if not self.pin == pin:
            raise InvalidPinError('incorrect pin')

    def get_account_number(self):
        return self.number

    def withdraw(self, pin: str, amount: int):
        self.validate_pin(pin)
        self.validate_amount(amount)
        self.validate_amount_limit(amount)
        self.balance -= amount

    def validate_amount_limit(self, amount):
        if self.balance < amount:
            raise InsufficientFundsError('insufficient funds')
