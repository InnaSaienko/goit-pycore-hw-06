import json
from functools import wraps
from addressbook import AddressBook
from records import Record
from fields_type import Name
from utils.validation_phone import validation_phone

with open("messages.json", encoding="utf-8") as f:
    MESSAGES = json.load(f)


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(e)
        except KeyError:
            print(MESSAGES["invalid_name"])
        except IndexError:
            print(MESSAGES["invalid_args"])

    return inner


def parse_input(user_input):
    parts = user_input.split()
    cmd, *args = parts
    cmd = cmd.lower()
    return cmd, args


@input_error
def handle_add(args, book: AddressBook):
    name, phone = args
    record = book.data.get(name)
    if record is None:
        record = Record(Name(name))
        record.add_phone(phone)
        book.add_record(record)
        return MESSAGES["contact_added"]
    else:
        record.add_phone(phone)
    return MESSAGES["change_success"]


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.data.get(name)
    old_phone = validation_phone(old_phone)
    new_phone = validation_phone(new_phone)

    if record:
        for phone in record.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return True
            return False
    return False


@input_error
def handle_change_contact(args, book):
    msg = MESSAGES["change_success"] if change_contact(args, book) else MESSAGES["contact_not_found"]
    return msg


@input_error
def show_phone(args, book):
    name = args[0]
    return book.get(name)


@input_error
def handle_show_phone(args, book):
    phone = show_phone(args, book)
    result = phone if phone else MESSAGES["contact_not_found"]
    return result


@input_error
def show_all(_args, book: AddressBook):
    if not book.data:
        return None
    return "\n".join(str(record) for record in book.data.values())


@input_error
def handle_show_all_contacts(_args, book: AddressBook):
    address_book = show_all(_args, book)
    result = MESSAGES["contact_list_empty"] if address_book is None else address_book
    return result


@input_error
def handle_add_birthday(args, book: AddressBook):
    name, date = args
    record = book.data.get(name)
    if record is None:
        return MESSAGES["birthday_contact_missing"]
    else:
        record.add_birthday(date)

    return MESSAGES["change_success"]


@input_error
def handle_show_birthday(self, name, book: AddressBook):
    record = book.data.get(name)
    if record in None:
        return MESSAGES["contact_not_found"]
    else:
        return record.birthday.value


def handle_welcome(_args, _contacts):
    return MESSAGES["welcome"]


@input_error
def handle_exit(_args, _contacts):
    raise StopIteration()
