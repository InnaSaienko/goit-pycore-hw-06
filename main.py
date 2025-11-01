from addressbook import AddressBook
from handlers import handle_exit, handle_welcome, handle_add, handle_change_contact, handle_show_phone, handle_show_all_contacts, parse_input, handle_add_birthday, handle_show_birthday

COMMAND_TO_HANDLER = {
    "add": handle_add,
    "change": handle_change_contact,
    "phone": handle_show_phone,
    "all": handle_show_all_contacts,
    "add-birthday": handle_add_birthday,
    "show-birthday": handle_show_birthday,
    # "birthday": handle_birthday,
    "hello": handle_welcome,
    "close": handle_exit,
    "exit": handle_exit,
}


def read_input():
    user_input = None
    try:
        while user_input is None:
            user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
    except EOFError:
        command, args = "exit", []
    return command, args


def process_command(command, args, book: AddressBook):
    try:
        handler = COMMAND_TO_HANDLER[command]
    except KeyError:
        print("Invalid command.")
    else:
        return handler(args, book)


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        try:
            command, args = read_input()
            result = process_command(command, args, book)
            print(result)
        except StopIteration:
            break
    print(f"Goodbye!")


if __name__ == "__main__":
    main()