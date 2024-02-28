import unittest

from my_diary.diary import Diary


class DiaryTest(unittest.TestCase):
    def test_diaryIsUnLockedOnCreationTest(self):
        diary = Diary("username", "password")
        self.assertEqual(False, diary.is_locked)  # add assertion here

    def test_lockDiary_diaryIsLocked(self):
        diary = Diary("username", "password")
        diary.lock_diary()
        self.assertEqual(True, diary.is_locked)

    def test_createEntry_entryListSizeIncreases(self):
        diary = Diary("username", "password")
        diary.add_entry("title", "body")
        self.assertEqual(1, diary.getListSize())

    def test_lockDiary_createEntry_listOfEntriesIsUnchanged(self):
        diary = Diary("username", "password")
        diary.lock_diary()
        diary.add_entry("title", "body")
        self.assertEqual(0, diary.getListSize())

    def test_createEntry_deleteEntry_listSizeReduces(self):
        diary = Diary("username", "password")
        diary.add_entry("title", "body")
        self.assertEqual(1, diary.getListSize())
        diary.delete_entry(1)
        self.assertEqual(0, diary.getListSize())

    def test_createEntry_findEntryById_returnsEntry(self):
        diary = Diary("username", "password")
        diary.add_entry("title", "body")
        found_entry = diary.find_entry_by_id(1)
        self.assertEqual(found_entry, diary.find_entry_by_id(1))

    def test_createEntry_updateEntry_entryIsUpdated(self):
        diary = Diary("username", "password")
        diary.add_entry("title", "body")
        found_entry = diary.find_entry_by_id(1)
        diary.update_entry(1, "new title", "new body")
        self.assertEqual(found_entry, diary.find_entry_by_id(1))
        print(found_entry)

    def test_createEntry_updateEntryWhileDiaryIsLocked_entryIsUnchanged(self):
        diary = Diary("username", "password")
        diary.add_entry("title", "body")
        found_entry = diary.find_entry_by_id(1)
        diary.update_entry(1, "new title", "new body")
        self.assertEqual(found_entry, diary.find_entry_by_id(1))
        print(found_entry)