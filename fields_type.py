from dataclasses import dataclass
from validation_phone import validation_phone


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