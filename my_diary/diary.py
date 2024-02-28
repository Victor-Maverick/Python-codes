from my_diary import entry
from my_diary.entry import Entry


class Diary:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.is_locked = False
        self.entries = []
        self.id_number = 0;

    def unlock_diary(self):
        self.is_locked = False

    def lock_diary(self):
        self.is_locked = True

    def is_locked(self):
        return self.is_locked

    def add_entry(self, title: str, body: str):
        if not self.is_locked:
            id_number = self.generate_id()
            new_entry = Entry(id_number, title, body)
            self.entries.append(new_entry)

    def generate_id(self):
        self.id_number += 1
        return self.id_number

    def getListSize(self):
        return len(self.entries)

    def delete_entry(self, id: int):
        found_entry = self.find_entry_by_id(id)
        self.entries.remove(found_entry)

    def find_entry_by_id(self, id: int):
        for eEntry in self.entries:
            if eEntry.id == id:
                return eEntry

    def update_entry(self, id: int, title: str, body: str):
        if self.is_locked:
            found_entry = self.find_entry_by_id(id)
            found_entry.set_title(title)
            found_entry.set_body(body)

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

