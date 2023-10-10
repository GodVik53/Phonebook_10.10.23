# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать 
# функционал для изменения и удаления данных.

# решение:

# запросили данные контакта для его сохранения
def name_data():
    return input("Введите имя: ")

def patronymic_data():
    return input("Введите отчество: ")

def surname_data():
    return input("Введите фамилию: ")

def phone_number_data():
    return input("Введите телефонный номер: ")

def address_data():
    return input("Введите адрес: ")

# создаем переменную для контакта
def input_contact():
    name = name_data()
    patronymic = patronymic_data()
    surname = surname_data()
    phone_number = phone_number_data()
    address = address_data()
    return f"{name} {patronymic} {surname}\n{phone_number}\n{address}"

# сохранили переменную, в которой записали контакт
def add_contact():
    contact = input_contact()
    with open("Pnonebook.txt", "a", encoding="utf-8") as data: #создаем текстовый файл, в который будет добавляться файл
        data.write(contact + "\n\n")                          # записали контакт в наш файл Phonebook.txt
    
def read_file():
    with open("Pnonebook.txt", "r", encoding="utf-8") as data: 
       return data.read()                          #  - это фунция чтения фйла. Считываем наш файл наш файл Phonebook.txt

def print_contact():                   # вывод записи контакта
    data = read_file()
    print()
    print(data)

# поиск контакта
def search_contact():
    print("Варианты поиска: \n"
            "1. По имени \n"
            "2. По фамилии \n"
            "3. По отчеству \n"
            "4. По номеру телефона \n"
            "5. По адресу ")
    choice = input("Выберите вариант поиска: ")
    i_choice = int(choice) - 1      #получили целочисленное
    search = input("Введите данные для поиска: ")
    data_str = read_file().rstrip()    # считать введенный файл (strip удаляет слева и справа пробельные символы вконце, если rstip - удалит справа, lsplit - удалит слева )
    if search not in data_str:
        print("Нет данных")
    else:
        #print([data_str])
        data_lst= data_str.split("\n\n") #выводим данные в строку
        #print(data_lst)
        for contact_str in data_lst:
            contact_lst = contact_str.replace("\n", " "). split()
            if search in contact_lst[i_choice]: #если поставить ==, то искать будет чётко по введенным данным, а не по схожести
                #print(contact_lst)
                print(contact_str)
                print()

# меняем запись контакта
def change_contact():
    print("Введите данные контакта, которые будем редактировать: ")
    contact = input_contact()
    data = read_file()
    if contact in data:
        print("Внесите изменения: ")
        new_contact = input_contact()
        with open("Pnonebook.txt", "w", encoding="utf-8") as data_new:
            data = data.replace(contact, new_contact)
            data_new.write(data)
    else:
        print("нет информации")


# удаляем запись контакта:
def delete_contact():
    print("Введите данные контакта, которого будем удалять: ")
    contact = input_contact()
    data = read_file()
    if contact in data:
        with open("Pnonebook.txt", "w", encoding="utf-8") as data_new:
            data = data.replace(contact + "\n\n", "")
            data_new.write(data)
    else:
        print("нет информации")


# создали интерфейс или меню
def user_interface():
    with open("Pnonebook.txt", "a", encoding="utf-8"): # создаем файл, если его нет
        pass # эта функция создает файл
    cmd = None
    while cmd != "4":
        print("Меню: \n"
            "1. Запись контакта \n"
            "2. Вывести данные на экран \n"
            "3. Поиск контакта \n"
            "4. Изменить контакт \n"
            "5. Удалить контакт\n"
            "6. Выход")

        cmd = input("Введите номер операции: ")

        while cmd not in ("1", "2","3","4", "5", "6"):
          print("Некорректный ввод")
          cmd = input ("Введите номер операции: ")

        match cmd:
         case "1":
            add_contact()
         case "2":
            print_contact()
         case "3":
            search_contact()
         case "4":
            change_contact() 
         case "5":
            delete_contact()  
         case "6":
            print("До свидания!")



user_interface()

