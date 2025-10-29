from dataclasses import dataclass
from datetime import datetime
from utils.validation_phone import validation_phone


@dataclass
class Field:
    value: str
    def __str__(self) -> str:
        return self.value

@dataclass
class Name(Field):
    value: str

@dataclass
class Phone(Field):
    value: str

    def __post_init__(self):
        self.value = validation_phone(self.value)


class Birthday(Field):
    value: datetime
    def __init__(self, value: str):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime("%Y.%m.%d")

