from BankApp.account import Account
from BankApp.account_not_found_error import AccountNotFoundError
from BankApp.invalid_amount_error import InvalidAmountError
from BankApp.invalid_pin_error import InvalidPinError


def validate_pin(found_account, pin):
    if not found_account.pin == pin:
        raise InvalidPinError('wrong pin')


def validate_amount_limit(amount, from_account):
    if from_account.balance < amount:
        raise InvalidAmountError("amount must be less than balance")


def validate_transfer_pin(from_account, pin):
    if not from_account.pin == pin:
        raise InvalidPinError("wrong pin")


class Bank:
    def __init__(self, name: str):
        self.name = name
        self.no_of_accounts = 0
        self.accounts = []

    def register_customer(self, first_name: str, last_name: str, pin: str):
        account_number = self.generate_number()
        account = Account(first_name + ' ' + last_name, account_number, pin)
        self.accounts.append(account)
        self.no_of_accounts += 1
        return account

    def generate_number(self) -> int:
        return self.no_of_accounts + 1

    def get_number_of_accounts(self) -> int:
        return len(self.accounts)

    def find_account(self, account_number: int) -> Account:
        for count in range(len(self.accounts)):
            if self.accounts[count].get_account_number() == account_number:
                return self.accounts[count]
        raise AccountNotFoundError("account not found")

    def deposit(self, account_number: int, amount: int):
        account: Account = self.find_account(account_number)
        account.deposit(amount)

    def get_balance(self, account_number: int, pin: str) -> int:
        account = self.find_account(account_number)
        return account.get_balance(pin)

    def remove(self, account_number: int, pin: str):
        found_account = self.find_account(account_number)
        validate_pin(found_account, pin)
        self.accounts.remove(found_account)
        pass

    def withdraw(self, account_number: int, pin: str, amount: int):
        found_account = self.find_account(account_number)
        found_account.withdraw(pin, amount)
        pass

    def transfer(self, sender_account_number, receiver_account_number, amount, pin):
        from_account = self.find_account(sender_account_number)
        to_account = self.find_account(receiver_account_number)
        validate_transfer_pin(from_account, pin)
        validate_amount_limit(amount, from_account)
        from_account.withdraw(pin, amount)
        to_account.deposit(amount)
