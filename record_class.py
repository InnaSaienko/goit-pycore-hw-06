from dataclasses import dataclass, field
from typing import List, Optional

from class_fields_templates import Name, Phone


@dataclass
class Record:
    name: Name
    phones: List[Phone] = field(default_factory=list)

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def find_phone(self, phone: str) -> Optional[Phone]:
        phone_generator = (p for p in self.phones if p.value == phone)
        return next(phone_generator, None)

    def remove_phone(self, phone: str) -> bool:
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
            return True
        return False

    def edit_phone(self, old_phone: str, new_phone: str) -> bool:
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return True
        return False

    def __str__(self):
        phone_str = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phone_str}"
