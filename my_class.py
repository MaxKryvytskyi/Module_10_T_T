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
    def __init__(self, name, phone=None):
        self.name = name
        self.phones = []
        if type(phone) == list:
            self.phones.extend(phone)
        else: 
            self.phones.append(phone)

    def add_phone(self, phone: Phone):
        if phone.value not in [phone.value for phone in self.phones]:
            self.phones.append(phone)
        else:
            print("This phone already added.")

    def remove_phone(self, phone: Phone):
        for n in self.phones:
            if n.value == phone.value:
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
