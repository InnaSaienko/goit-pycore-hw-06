from addressbook import AddressBook
from records import Record
from fields_type import Name, Phone, Birthday


def main():
    book = AddressBook()

    john_record = Record(Name("John"), Birthday("01.01.1990"))
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    # john_record.add_birthday("01.01.1990")
    book.add_record(john_record)

    jane_record = Record(Name("Jane"), Birthday("02.11.1992"))
    jane_record.add_phone("9876543210")
    # jane_record.add_birthday("02.11.1992")
    book.add_record(jane_record)

    # Show all records
    print("All contacts:")
    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    upcoming_birthdays = book.get_upcoming_birthdays()
    print(f"\nUpcoming birthdays: {upcoming_birthdays}")

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    book.delete("Jane")


if __name__ == "__main__":
    main()