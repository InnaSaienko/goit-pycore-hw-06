from dataclasses import dataclass, field
from typing import List

from class_fields_templates import Name, Phone


@dataclass
class Record:
    name: Name
    phone: List[Phone] = field(default_factory=List)

    def add_phone(self, phone: str) -> None:
        pass

    def remove_phone(self, phone: str) -> None:
        pass

    def edit_phone(self, phone: str) -> None:
        pass

    def find_phone(self, phone: str) -> None:
        pass