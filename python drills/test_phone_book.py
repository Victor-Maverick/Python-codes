import unittest
import phone_book


class TestPhoneBook(unittest.TestCase):

    def test_add_contact_to_list_contact_list_adds(self):
        self.assertEqual(0, phone_book.length_of_contact_list())
        phone_book.add_contact("victor", "08148624687")
        self.assertEqual(1, phone_book.length_of_contact_list())
        phone_book.add_contact("vic", "08148624688")
        self.assertEqual(2, phone_book.length_of_contact_list())
        phone_book.delete_list()

    def test_add_contact_to_list_contact_list_remains_unchanged(self):
        self.assertEqual(0, phone_book.length_of_contact_list())
        phone_book.add_contact("victor", "08148624687")
        self.assertEqual(1, phone_book.length_of_contact_list())
        phone_book.add_contact("victor", "08148624687")
        self.assertEqual(1, phone_book.length_of_contact_list())
        phone_book.delete_list()

    def test_delete_contact_by_name_from_list_list_decreases(self):
        self.assertEqual(0, phone_book.length_of_contact_list())
        phone_book.add_contact("victor", "08148624687")
        self.assertEqual(1, phone_book.length_of_contact_list())
        phone_book.delete_contact_by_name("victor")
        self.assertEqual(0, phone_book.length_of_contact_list())
        phone_book.delete_list()

    def test_delete_contact_by_name_from_list_list_remains_unchanged(self):
        self.assertEqual(0, phone_book.length_of_contact_list())
        phone_book.add_contact("victor", "08148624687")
        self.assertEqual(1, phone_book.length_of_contact_list())
        phone_book.add_contact("victor", "08148624687")
        self.assertEqual(1, phone_book.length_of_contact_list())
        phone_book.add_contact("vic", "08148624688")
        self.assertEqual(2, phone_book.length_of_contact_list())
        phone_book.delete_contact_by_name("vic")
        phone_book.delete_contact_by_name("vic")
        self.assertEqual(1, phone_book.length_of_contact_list())
        phone_book.delete_list()

    def test_delete_contact_by_number_from_list_list_decreases(self):
        self.assertEqual(0, phone_book.length_of_contact_list())
        phone_book.add_contact("victor", "08148624687")
        self.assertEqual(1, phone_book.length_of_contact_list())
        phone_book.delete_contact_by_number("08148624687")
        self.assertEqual(0, phone_book.length_of_contact_list())
        phone_book.delete_list()

    def test_delete_contact_by_number_from_list_list_remains_unchanged(self):
        self.assertEqual(0, phone_book.length_of_contact_list())
        phone_book.add_contact("victor", "08148624687")
        self.assertEqual(1, phone_book.length_of_contact_list())
        phone_book.add_contact("victor", "08148624687")
        self.assertEqual(1, phone_book.length_of_contact_list())
        phone_book.add_contact("vic", "08148624688")
        self.assertEqual(2, phone_book.length_of_contact_list())
        phone_book.delete_contact_by_number("08148624688")
        phone_book.delete_contact_by_number("08148624688")
        self.assertEqual(1, phone_book.length_of_contact_list())
        phone_book.delete_list()
