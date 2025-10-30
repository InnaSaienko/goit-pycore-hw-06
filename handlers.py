import sys
from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Give me name and phone please.")
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
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return True
    return False


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts.get(name)


@input_error
def show_all(_args, contacts):
    if contacts:
        return "\n".join(f"{n}: {p}" for n, p in contacts.items())
    return None


@input_error
def handle_exit(_args, _contacts):
    raise StopIteration()


def handle_welcome(_args, _contacts):
    print(f"How can I help you?")


@input_error
def handle_add(args, contacts):
    add_contact(args, contacts)
    print("Contact added.")


@input_error
def handle_change_contact(args, contacts):
    msg = "Contact updated." if change_contact(args, contacts) else "Contact not found."
    print(msg)


@input_error
def handle_show_phone(args, contacts):
    phone = show_phone(args, contacts)
    msg = phone if phone else "Contact not found."
    print(msg)


@input_error
def handle_show_all_contacts(contacts):
    contacts_str = show_all(contacts)
    if contacts_str is None:
        contacts_str = "No contacts found."
    print(contacts_str)
