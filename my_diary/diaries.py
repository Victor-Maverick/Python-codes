from diary_not_found_error import DiaryNotFoundError
from my_diary.diary import Diary
from my_diary.invalid_password_error import InvalidPasswordError


class Diaries:
    def __init__(self):
        self.diaries = []

    def add(self, username: str, password: str):
        diary = Diary(username, password)
        self.diaries.append(diary)

    def get_list_size(self):
        return len(self.diaries)

    def find_by_username(self, username: str) -> Diary:
        if self.get_list_size() == 0:
            raise DiaryNotFoundError("diary not found")
        for diary in self.diaries:
            if diary.get_username() == username:
                return diary

        raise DiaryNotFoundError("diary not found")
    def delete(self, username: str, password: str):
        found_entry = self.find_by_username(username)
        if found_entry is None:
            raise DiaryNotFoundError("diary not found")
        if not found_entry.get_password() == password:
            raise InvalidPasswordError("wrong password")
        self.diaries.remove(found_entry)
