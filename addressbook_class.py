from collections import UserDict
from typing import Optional
from record_class import Record


class AddressBook(UserDict):

    def add_record(self, record: Record) -> None:
        pass

    def find(self, name: str) -> Optional[Record]:
        pass

    def delete(self, name: str) -> bool:
        pass