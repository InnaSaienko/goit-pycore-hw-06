from collections import UserDict
from typing import Optional
from records import Record
from utils.get_upcoming_birthdays import get_birthdays


class AddressBook(UserDict):

    def add_record(self, record: Record) -> bool:
        self.data[record.name.value] = record
        return True

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name)

    def delete(self, name: str) -> bool:
        if name in self.data:
            del self.data[name]
            return True
        else:
            return False

    def get_upcoming_birthdays(self):
        return get_birthdays(self.data)