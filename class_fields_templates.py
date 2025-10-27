from dataclasses import dataclass


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
    phone: str

