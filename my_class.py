from collections import UserDict


class AddtextsBook(UserDict):
    def add_record(self, record):
        if record.name.value not in self.keys():
            self.data[record.name.value] = record
        else:
            print("Name already exist. Try add phone command for add extra phone.")


class Field:
    def __init__(self, value=None):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name, phones=None):
        self.name = name
        self.phones = []
        if type(phones) == list:
            self.phones.extend(phones)
        else: 
            self.phones.append(phones)

    def add_phone(self, phones: Phone):
        if phones.value not in [phones.value for phones in self.phones]:
            self.phones.append(phones)
        else:
            print("This phone already added.")

    def remove_phone(self, phones: Phone):
        for n in self.phones:
            if n.value == phones.value:
                self.phones.remove(n)

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        if old_phone.value == new_phone.value or new_phone.value in [phone.value for phone in self.phones]:
            print("This phone alredy exist!")
        elif old_phone.value not in [phone.value for phone in self.phones]:
            print("This phone not found!")
        else:
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
            print("Phone changed.")
