import unittest

from BankApp.account import Account
from BankApp.insufficient_funds_error import InsufficientFundsError
from BankApp.invalid_amount_error import InvalidAmountError
from BankApp.invalid_pin_error import InvalidPinError


class AccountTest(unittest.TestCase):

    def test_depositPositiveAmount_balanceIncreases(self):
        account = Account("correctPin")
        account.deposit(200)
        self.assertEqual(200, account.get_balance("correctPin"))

    def test_checkBalanceWithWrongPin_raiseInvalidPinError(self):
        account = Account("correctPin")
        with self.assertRaises(InvalidPinError):
            account.get_balance("incorrectPin")

    def test_depositTwice_balanceIncreasesTwice(self):
        account = Account("correctPin")
        account.deposit(200)
        self.assertEqual(200, account.get_balance("correctPin"))
        account.deposit(200)
        self.assertEqual(400, account.get_balance("correctPin"))

    def test_depositNegativeAmount_raisesError(self):
        account = Account("correctPin")
        with self.assertRaises(InvalidAmountError):
            account.deposit(-122)

    def test_deposit_withdrawWithCorrectPin_balanceDecreasesTest(self):
        account = Account("correctPin")
        account.deposit(200)
        self.assertEqual(200, account.get_balance("correctPin"))
        account.withdraw("correctPin", 100)
        self.assertEqual(100, account.get_balance("correctPin"))

    def test_deposit_withdrawNegativeAmount_raisesInvalidAmountError(self):
        account = Account("correctPin")
        account.deposit(200)
        self.assertEqual(200, account.get_balance("correctPin"))

        with self.assertRaises(InvalidAmountError):
            account.withdraw("correctPin", -100)
        self.assertEqual(200, account.get_balance("correctPin"))

    def test_deposit_withdrawWithIncorrectPin_raisesError(self):
        account = Account("correctPin")
        account.deposit(200)
        self.assertEqual(200, account.get_balance("correctPin"))

        with self.assertRaises(InvalidPinError):
            account.withdraw("incorrectPin", 100)
        self.assertEqual(200, account.get_balance("correctPin"))

    def test_deposit_withdrawMoreThanBalance_raisesInsufficientFundsError(self):
        account = Account("correctPin")
        account.deposit(200)
        self.assertEqual(200, account.get_balance("correctPin"))

        with self.assertRaises(InsufficientFundsError):
            account.withdraw("correctPin", 500)
        self.assertEqual(200, account.get_balance("correctPin"))
