import re


import my_class as oop


adress_book = oop.AddtextsBook()
flag_exit = True

# Обробка помилок.
def input_error(func):
    def inner(*argsi,**kwargs): 
        try:
            return func(*argsi,**kwargs)
        except TypeError:
            print("Wrong command")
            return main()
        except IndexError:
            print('Enter name and phone separated by a space!')
            return main()
        except ValueError:
            print("ValueError") # що повинно статися щоб побачити тебе?
            return main()
        except KeyError:
            print("Enter another name.")
            return main()
        except AttributeError:
            print('Enter command.')
            return main()
    return inner

# Асистент вітається у відповідь.
@input_error
def hello(_):
    return "How can I help you?"

# Асистент додає дані до книги контактів.
@input_error
def add(uzer_input):
    text = uzer_input.split()
    rec = oop.Record(oop.Name(text[1].capitalize()), [oop.Phone(text[2])])
    adress_book.add_record(rec)
    return f"Контакт {text[1].capitalize()} з номером {text[2]} створений"

# Асистент змінює дані в книзі контактів.
@input_error
def change(uzer_input):
    text = uzer_input.split()
    return f"Номер телефона {text[1].capitalize()} змінений на : {text[2]}"

# Заміна телефону A на телефон B 
@input_error
def change(uzer_input):
    text = uzer_input.split()
    rec = adress_book[text[1].capitalize()]
    ret = f"{rec.name.value} : {[phone.value for phone in adress_book[rec.name.value].phones]}\n" + "Змінено на\n"
    rec.edit_phone(oop.Phone(text[2]), oop.Phone(text[3]))
    ret += f"{rec.name.value} : {[phone.value for phone in rec.phones]}"
    return ret
    
# Ассистент за ім'ям знаходить в контактах номер.
@input_error
def phone(uzer_input):
    text = uzer_input.split()
    text = [i.capitalize() for i in text]
    rec = adress_book[text[1]]
    return f"Номер телефону {text[1]} це : {[phone.value for phone in rec.phones]}"

# Видаляє мобільний телефон
@input_error
def remove_phones(uzer_input):
    text = uzer_input.split()
    rec = adress_book[text[2].capitalize()]
    rec.remove_phone(oop.Phone(text[3]))
    return f"Номер телефону {text[2]} : {text[3]}\nВидалений"

# Ассистент показує всі контактні дані.
@input_error
def show_all(_):
    text = ''
    for key, record in adress_book.items():
        text += f"{key} : {[phone.value for phone in record.phones]}\n"
    return text if text else "Addtexts book is empty."

# Зупиняє роботу асистента.
@input_error
def exit_uzer(_):
    global flag_exit
    flag_exit = False
    return "Good bye!"

# Список команд.
COMMANDS = {"hello": hello, # Виводить привітання
            "add" : add, # Додає контакт в книгу контактів 
            "change": change, #
            "phone" : phone, # Виводить номер телефону за ім'ям
            "show all" : show_all, # Показує книгу контактів
            "good bye" : exit_uzer, # Виходить з асистента
            "close" : exit_uzer, # Виходить з асистента
            "exit" : exit_uzer, # Виходить з асистента
            "remove phone" : remove_phones # Видаляє телефон 
            }

# Знаходить команду.
@input_error    
def handler(uzer_input):
    text = uzer_input.lower()
    for keys in COMMANDS.keys():
        if re.findall(text, keys):
            return COMMANDS[keys]
        
# Знаходить команду.
@input_error    
def handler(uzer_input):
    text = uzer_input.lower()
    found_keywords = []
    for keyword in COMMANDS.keys():
        if text.find(keyword) != -1:
            found_keywords.append(keyword)
    comannds = list(filter(lambda x: len(x) == max(len(com) for com in found_keywords), found_keywords))
    print(comannds[0])
    return COMMANDS[comannds[0]]

@input_error
def main():
    while flag_exit:
        uzer_input = input("-->")
        com = handler(uzer_input)
        print(com(uzer_input.lower()))

if __name__ == "__main__":
    main()