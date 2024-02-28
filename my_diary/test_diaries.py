import unittest

from diary_not_found_error import DiaryNotFoundError
from my_diary.diaries import Diaries
from my_diary.invalid_password_error import InvalidPasswordError


class MyTestCase(unittest.TestCase):
    def test_createDiary_addDiaryToList_listSizeIncreases(self):
        diaries = Diaries()
        diaries.add("username", "password")
        self.assertEqual(1, diaries.get_list_size())  # add assertion here

    def test_addDiaryToDiaries_findByUsername_returnsDiaryCreated(self):
        diaries = Diaries()
        diaries.add("username", "password")
        found_entry = diaries.find_by_username("username")
        self.assertEqual(found_entry, diaries.find_by_username("username"))

    def test_createDiary_deleteADiary_diaryListDecreases(self):
        diaries = Diaries()
        diaries.add("username", "password")
        diaries.delete("username", "password")
        self.assertEqual(0, diaries.get_list_size())

    def test_createDiary_deleteDiaryWithWrongPassword_throwsError(self):
        diaries = Diaries()
        diaries.add("username", "password")
        with self.assertRaises(InvalidPasswordError):
            diaries.delete("username", "wrong password")
        self.assertEqual(1, diaries.get_list_size())

    def test_deleteNonExistingDiary_throwsDiaryNotFoundError(self):
        diaries = Diaries()
        with self.assertRaises(DiaryNotFoundError):
            diaries.delete("username", "password")

    def test_findNonExistingDiary_throwsDiaryNotFoundError(self):
        diaries = Diaries()
        with self.assertRaises(DiaryNotFoundError):
            diaries.find_by_username("username")

    def test_findDiaryInEmptyList_throwsDiaryNotFoundError(self):
        diaries = Diaries()
        diaries.add("username", "password")
        with self.assertRaises(DiaryNotFoundError):
            diaries.find_by_username("wrong username")
