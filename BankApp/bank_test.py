import unittest

from BankApp.account import Account
from BankApp.bank import Bank
from BankApp.insufficient_funds_error import InsufficientFundsError
from BankApp.invalid_amount_error import InvalidAmountError
from BankApp.invalid_pin_error import InvalidPinError


def setInitial():
    gtBank = Bank("GTBank")


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.gtBank = Bank("GT Bank")

    def tearDown(self):
        print('tear')

    def test_createAccount_listOfAccountIncreases(self):
        account = self.gtBank.register_customer("firstName", "lastName", "correctPin")
        self.assertEqual(1, self.gtBank.get_number_of_accounts())

    def test_createAccount_accountCanBeFoundInListOfAccounts(self):
        account: Account = self.gtBank.register_customer("firstName", "lastName", "correctPin")
        self.assertEqual(account, self.gtBank.find_account(1))

    def test_registerCustomer_depositPositiveAmount_balanceIncreases(self):
        account = self.gtBank.register_customer("firstName", "lastName", "correctPin")
        self.gtBank.deposit(1, 1000)
        self.assertEqual(1000, self.gtBank.get_balance(1, "correctPin"))
        self.assertEqual(account, self.gtBank.find_account(1))

    def test_registerCustomer_depositNegativeAmount_raisesError(self):
        self.gtBank.register_customer("firstName", "lastName", "correctPin")
        with self.assertRaises(InvalidAmountError):
            self.gtBank.deposit(1, -1000)
        self.assertEqual(0, self.gtBank.get_balance(1, "correctPin"))

    def test_checkBalanceWithWrongPin_raisesInvalidPinError(self):
        self.gtBank.register_customer("firstName", "lastName", "correctPin")
        with self.assertRaises(InvalidPinError):
            self.gtBank.get_balance(1, "incorrectPin")

    def test_registerCustomer_removeCustomer_listOfAccountsIsEmpty(self):
        self.gtBank.register_customer("firstName", "lastName", "correctPin")
        self.gtBank.remove(1, "correctPin")
        self.assertEqual(0, self.gtBank.get_number_of_accounts())

    def test_registerThreeCustomers_removeSecondCustomer_findThirdAccount_returnsThirdAccount(self):
        self.gtBank.register_customer("firstName", "lastName", "correctPin")
        self.gtBank.register_customer("firstName", "lastName", "Pin")
        account3 = self.gtBank.register_customer("firstName", "last Name", "correctPin")
        self.gtBank.remove(2, "Pin")
        self.assertEqual(account3, self.gtBank.find_account(3))
        self.assertEqual(2, self.gtBank.get_number_of_accounts())

    def test_registerCustomer_removeCustomerWithWrongPin_raisesInvalidPinError(self):
        account1 = self.gtBank.register_customer("firstName", "lastName", "correctPin")
        with self.assertRaises(InvalidPinError):
            self.gtBank.remove(1, "incorrectPin")
        self.assertEqual(account1, self.gtBank.find_account(1))
        self.assertEqual(1, self.gtBank.get_number_of_accounts())

    def test_registerAccount_deposit_withdrawPositiveAmount_balanceDecreases(self):
        account = self.gtBank.register_customer("firstName", "lastName", "correctPin")
        self.gtBank.deposit(1, 5000)
        self.gtBank.withdraw(1, "correctPin", 3000)
        self.assertEqual(2000, account.get_balance("correctPin"))

    def test_registerAccount_deposit_withdrawWithWrongPin_raiseInvalidPinError(self):
        account = self.gtBank.register_customer("firstName", "lastName", "correctPin")
        self.gtBank.deposit(1, 5000)
        with self.assertRaises(InvalidPinError):
            self.gtBank.withdraw(1, "incorrectPin", 3000)
        self.assertEqual(5000, account.get_balance("correctPin"))

    def test_registerAccount_deposit_withdrawMoreThanBalance_raiseInsufficientFundsError(self):
        account = self.gtBank.register_customer("firstName", "lastName", "correctPin")
        self.gtBank.deposit(1, 5000)
        with self.assertRaises(InsufficientFundsError):
            self.gtBank.withdraw(1, "correctPin", 8000)
        self.assertEqual(5000, account.get_balance("correctPin"))

    def test_registerAccount_deposit_withdrawNegativeAmount_raiseInvalidAmountError(self):
        account = self.gtBank.register_customer("firstName", "lastName", "correctPin")
        self.gtBank.deposit(1, 5000)
        with self.assertRaises(InsufficientFundsError):
            self.gtBank.withdraw(1, "correctPin", 8000)
        self.assertEqual(5000, account.get_balance("correctPin"))

    def test_registerTwoAccounts_depositFirstAccount_transferFromFirstToSecond_bothBalancesChange(self):
        account1 = self.gtBank.register_customer("firstName", "lastName", "correctPin")
        account2 = self.gtBank.register_customer("firstName", "lastName", "Pin")
        self.gtBank.deposit(1, 4000)
        self.gtBank.transfer(account1.number, account2.number, 2000, "correctPin")
        self.assertEqual(2000, account1.get_balance("correctPin"))
        self.assertEqual(2000, account2.get_balance("Pin"))