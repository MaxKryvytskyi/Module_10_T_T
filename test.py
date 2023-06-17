from collections import UserDict


class AddressBook(UserDict):
    def addRecord(self,record):
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
    def __init__(self,name, phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)


    def add_phone(self, phone: Phone):
        if phone.value not in [phone.value for phone in self.phones]:
            self.phones.append(phone)
        else:
            print("This phone already added.")


    def del_phone(self, phone: Phone):
        for n in self.phones:
            if n.value == phone.value:
                self.phones.remove(n)


    def change_phone(self,old_phone: Phone, new_phone: Phone):
        if old_phone.value == new_phone.value or new_phone.value in [phone.value for phone in self.phones]:
            print("This phone alredy exist!")
        elif old_phone.value not in [phone.value for phone in self.phones]:
            print("This phone not found!")
        else:
            self.del_phone(old_phone)
            self.add_phone(new_phone)
            print("Phone changed.")


adress_book = AddressBook()
print(adress_book.data)
# add_record
rec = Record(Name("bill"), Phone("123132321"))
print(adress_book.data)
adress_book.addRecord(rec)
print(adress_book.data)
print(f"{rec.name.value} : {[ phone.value for phone in adress_book[rec.name.value].phones]}\n")

rec11 = Record(Name("klara"), Phone("11"))
print(adress_book.data)
adress_book.addRecord(rec11)
print(adress_book.data)
print(f"{rec11.name.value} : {[ phone.value for phone in adress_book[rec11.name.value].phones]}\n")

rec111 = Record(Name("gena"), Phone("121"))
print(adress_book.data)
adress_book.addRecord(rec111)
print(adress_book.data)
print(f"{rec111.name.value} : {[ phone.value for phone in adress_book[rec111.name.value].phones]}\n")



# change_phone
rec = adress_book["bill"]
print(f"{rec.name.value} : {[ phone.value for phone in adress_book[rec.name.value].phones]}\n")
rec.change_phone(Phone("123132321"),Phone("1"))
print(f"{rec.name.value} : {[ phone.value for phone in rec.phones]}\n")

# add_record
rec1 = Record(Name("Ted"), Phone("2"))
print(adress_book.data)
adress_book.addRecord(rec1)
print(adress_book.data)
print(f"{rec1.name.value} : {[phone.value for phone in adress_book[rec1.name.value].phones]}\n")


# delete_phone
print(adress_book.data)
rec3 = adress_book["Ted"]
rec3.del_phone(Phone("2"))
print(adress_book.data)
print(f"{rec3.name.value} : {[ phone.value for phone in rec3.phones]}\n")

# phone
rec = adress_book["bill"]
print(f"{rec.name.value} : {[ phone.value for phone in rec.phones]}")

# show all
res = ''
source = adress_book
for key, record in source.items():
    res += f"{key} : {[ phone.value for phone in record.phones]}\n"
print(res if res else "Address book is empty.")

print(adress_book.data)




# adress_book = AddtextsBook()

# # Додаємо контакт в словник *
 

# # rec = Record(Name("Bill"), [Phone("0")])
# # adress_book.add_record(rec)
# # print(adress_book.data)
# # print(f"{rec.name.value} : {[phone.value for phone in adress_book[rec.name.value].phones]}\n")

# # rec1 = Record(Name("Ted"), [Phone("1")])
# # adress_book.add_record(rec1)
# # print(adress_book.data)
# # print(f"{rec1.name.value} : {[phone.value for phone in adress_book[rec1.name.value].phones]}\n")

# # rec2 = Record(Name("Gerard"), [Phone("2")])
# # adress_book.add_record(rec2)
# # print(adress_book.data)
# # print(f"{rec2.name.value} : {[phone.value for phone in adress_book[rec2.name.value].phones]}\n")

# # rec3 = Record(Name("Timmi"), [Phone("3"), Phone("33")])
# # adress_book.add_record(rec3)
# # print(adress_book.data)
# # print(f"{rec3.name.value} : {[phone.value for phone in adress_book[rec3.name.value].phones]}\n")

# # rec4 = Record(Name("Max"), [Phone("4"), Phone("44"), Phone("444")])
# # adress_book.add_record(rec4)
# # print(adress_book.data)
# # print(f"{rec4.name.value} : {[phone.value for phone in adress_book[rec4.name.value].phones]}\n")


# # Заміна телефону A на телефон B 

# '''
# rec5 = adress_book["Bill"]
# print(f"{rec5.name.value} : {[phone.value for phone in adress_book[rec5.name.value].phones]}")
# rec5.edit_phone(Phone("0"), Phone("0000"))
# print(f"{rec5.name.value} : {[phone.value for phone in rec5.phones]}\n")

# rec6 = adress_book["Ted"]
# print(f"{rec6.name.value} : {[phone.value for phone in adress_book[rec6.name.value].phones]}")
# rec6.edit_phone(Phone("1"), Phone("1111"))
# print(f"{rec6.name.value} : {[phone.value for phone in rec6.phones]}\n")

# rec7 = adress_book["Gerard"]
# print(f"{rec7.name.value} : {[phone.value for phone in adress_book[rec7.name.value].phones]}")
# rec7.edit_phone(Phone("2"), Phone("2222"))
# print(f"{rec7.name.value} : {[phone.value for phone in rec7.phones]}\n")

# rec8 = adress_book["Timmi"]
# print(f"{rec8.name.value} : {[phone.value for phone in adress_book[rec8.name.value].phones]}")
# rec8.edit_phone(Phone("3"), Phone("3333"))
# print(f"{rec8.name.value} : {[phone.value for phone in rec8.phones]}\n")

# rec9 = adress_book["Max"]
# print(f"{rec9.name.value} : {[phone.value for phone in adress_book[rec9.name.value].phones]}")
# rec9.edit_phone(Phone("4"), Phone("4444"))
# print(f"{rec9.name.value} : {[phone.value for phone in rec9.phones]}\n")'''

# # Показати телефон за ім'ям *

# # rec10 = adress_book["Bill"]
# # print(f"{rec10.name.value} : {[phone.value for phone in rec10.phones]}\n")

# # rec11 = adress_book["Ted"] 
# # print(f"{rec11.name.value} : {[phone.value for phone in rec11.phones]}\n")

# # rec12 = adress_book["Gerard"] 
# # print(f"{rec12.name.value} : {[phone.value for phone in rec12.phones]}\n")

# # rec13 = adress_book["Timmi"] 
# # print(f"{rec13.name.value} : {[phone.value for phone in rec13.phones]}\n")

# # rec14 = adress_book["Max"] 
# # print(f"{rec14.name.value} : {[phone.value for phone in rec14.phones]}\n")

# # Видаляє телефон *

# # rec15 = adress_book["Max"]
# # rec15.remove_phone(Phone("444"))
# # print(f"{rec15.name.value} : {[ phone.value for phone in rec15.phones]}\n")

# # Виводить книгу контактів *

# # text = ''
# # for key, record in adress_book.items():
# #     text += f"{key} : {[phone.value for phone in record.phones]}\n"
# # print(text if text else "Addtexts book is empty.")













# # # Додаємо контакт в словник 

# # rec = oop.Record(oop.Name("Bill"), [oop.Phone("0")])
# # adress_book.add_record(rec)
# # print(adress_book.data)
# # print(f"{rec.name.value} : {[phone.value for phone in adress_book[rec.name.value].phones]}\n")

# # rec1 = oop.Record(oop.Name("Ted"), [oop.Phone("1")])
# # adress_book.add_record(rec1)
# # print(adress_book.data)
# # print(f"{rec1.name.value} : {[phone.value for phone in adress_book[rec1.name.value].phones]}\n")

# # rec2 = oop.Record(oop.Name("Gerard"), [oop.Phone("2")])
# # adress_book.add_record(rec2)
# # print(adress_book.data)
# # print(f"{rec2.name.value} : {[phone.value for phone in adress_book[rec2.name.value].phones]}\n")

# # rec3 = oop.Record(oop.Name("Timmi"), [oop.Phone("3"), oop.Phone("33")])
# # adress_book.add_record(rec3)
# # print(adress_book.data)
# # print(f"{rec3.name.value} : {[phone.value for phone in adress_book[rec3.name.value].phones]}\n")

# # rec4 = oop.Record(oop.Name("Max"), [oop.Phone("4"), oop.Phone("44"), oop.Phone("444")])
# # adress_book.add_record(rec4)
# # print(adress_book.data)
# # print(f"{rec4.name.value} : {[phone.value for phone in adress_book[rec4.name.value].phones]}\n")

# # # Заміна телефону A на телефон B 

# # rec5 = adress_book["Bill"]
# # print(f"{rec5.name.value} : {[phone.value for phone in adress_book[rec5.name.value].phones]}")
# # rec5.edit_phone(oop.Phone("0"), oop.Phone("0000"))
# # print(f"{rec5.name.value} : {[phone.value for phone in rec5.phones]}\n")

# # rec6 = adress_book["Ted"]
# # print(f"{rec6.name.value} : {[phone.value for phone in adress_book[rec6.name.value].phones]}")
# # rec6.edit_phone(oop.Phone("1"), oop.Phone("1111"))
# # print(f"{rec6.name.value} : {[phone.value for phone in rec6.phones]}\n")

# # rec7 = adress_book["Gerard"]
# # print(f"{rec7.name.value} : {[phone.value for phone in adress_book[rec7.name.value].phones]}")
# # rec7.edit_phone(oop.Phone("2"), oop.Phone("2222"))
# # print(f"{rec7.name.value} : {[phone.value for phone in rec7.phones]}\n")

# # rec8 = adress_book["Timmi"]
# # print(f"{rec8.name.value} : {[phone.value for phone in adress_book[rec8.name.value].phones]}")
# # rec8.edit_phone(oop.Phone("3"), oop.Phone("3333"))
# # print(f"{rec8.name.value} : {[phone.value for phone in rec8.phones]}\n")

# # rec9 = adress_book["Max"]
# # print(f"{rec9.name.value} : {[phone.value for phone in adress_book[rec9.name.value].phones]}")
# # rec9.edit_phone(oop.Phone("4"), oop.Phone("4444"))
# # print(f"{rec9.name.value} : {[phone.value for phone in rec9.phones]}\n")

