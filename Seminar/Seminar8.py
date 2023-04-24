'''
Создать телефонный справочник с возможностью импорта и экспорта данных в 
формате .txt. Фамилия, имя, отчество, номер телефона - данные, 
которые должны находиться в файле.
Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска определенной 
записи(Например имя или фамилию человека)
Использование функций. Ваша программа не должна быть линейной

def add_user():
    last_name = input("Input last name: ")
    first_name = input("Input first name: ")
    surname = input("Input surname name: ")
    phone = input("Input phone number: ")
    data = open("phone_book.txt", "a", encoding = "utf-8")
    data.writelines([last_name + " ", first_name + " ", surname + " ", phone + "\n"])
    data.close()

def print_data():
    with open("phone_book.txt", "r", encoding = "utf-8") as data:
        print(data.read())

def search():
    search_data = input("Input key word to search in file: ")
    with open("phone_book.txt", "r", encoding = "utf-8") as data:
        for line in data:
            if search_data in line:
                print(line)

def load_data():
    with open("phone_book.txt", "r+", encoding = "utf-8") as data:
        textdata = data.read()
        path = input("Input file: ")
        with open(path, "r", encoding = "utf-8") as data2:
            for line in data2:
                if line not in textdata:
                    data.write(line)

def ui():
    print("""1: Add user
2: Search user
3: Import from file
4: Console output""")
    user_input = input("Input number: ")
    if user_input == "1":
        add_user()
    elif user_input == "2":
        search()
    elif user_input == "3":
        load_data()
    elif user_input == "4":
        print_data()
    else:
        print("Incorrect")

def main():
    ui()

if __name__ == "__main__":
    main()
'''