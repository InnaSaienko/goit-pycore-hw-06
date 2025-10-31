from functools import wraps
from addressbook import AddressBook
from records import Record
from fields_type import Name


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(e)
        except KeyError:
            print("Invalid name.")
        except IndexError:
            print("A username is required.")

    return inner

def parse_input(user_input):
    parts = user_input.split()
    cmd, *args = parts
    cmd = cmd.lower()
    return cmd, args

@input_error
def get_contact(name, book: AddressBook):
    return book.data.get(name)

@input_error
def handle_add(args, book: AddressBook):
    name, phone = args
    record = get_contact(name, book)
    message = "Contact updated."
    if record is None:
        record = Record(Name(name))
        record.add_phone(phone)
        book.add_record(record)
        message = "Contact added."
    else:
        record.add_phone(phone)
    print(message)

@input_error
def change_contact(args, book: AddressBook):
    name, phone = args
    if name in book:
        book[name] = phone
        return True
    return False

@input_error
def handle_change_contact(args, contacts):
    msg = "Contact updated." if change_contact(args, contacts) else "Contact not found."
    print(msg)

@input_error
def show_phone(args, book):
    name = args[0]
    return book.get(name)

@input_error
def handle_show_phone(args, book):
    phone = show_phone(args, book)
    msg = phone if phone else "Contact not found."
    print(msg)

@input_error
def show_all(_args, book: AddressBook):
    if not book.data:
        return None
    return "\n".join(str(record) for record in book.data.values())

@input_error
def handle_show_all_contacts(_args, book: AddressBook):
    result = show_all(_args, book)
    if result is None:
        result = "No contacts found."
    print(result)

@input_error
def handle_add_birthday(args, book: AddressBook):
    name, date = args
    record = get_contact(name, book)
    message = "Contact updated."
    if record is None:
        message = "Can't update, the contact doesn't exist."
    else:
        record.add_birthday(date)
    print(message)


def handle_welcome(_args, _contacts):
    print(f"How can I help you?")

@input_error
def handle_exit(_args, _contacts):
    raise StopIteration()
