import re

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

def delete():
    deletedata = input("Input max info about user to delete: ")
    with open("phone_book.txt") as data:
        lines = data.readlines()
    pattern = re.compile(re.escape(deletedata))
    with open("phone_book.txt", 'w') as data:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                data.write(line)
    print(f"List without {deletedata}: ")
    with open("phone_book.txt", "r", encoding = "utf-8") as data:
        print(data.read())

def change():
    old_info = input("Input old last_name, first_name, surname and phone: ")
    new_info = input("Input new last_name, first_name, surname and phone: ")
    with open ("phone_book.txt", 'r') as data:
        old_data = data.read()
    new_data = old_data.replace(old_info, new_info)
    with open ("phone_book.txt", 'w') as data:
        data.write(new_data)

def ui():
    print("""1: Add user
2: Search user
3: Import from file
4: Console output
5: Delete user
6: Change info""")
    user_input = input("Input number: ")
    if user_input == "1":
        add_user()
    elif user_input == "2":
        search()
    elif user_input == "3":
        load_data()
    elif user_input == "4":
        print_data()
    elif user_input == "5":
        delete()
    elif user_input == "6":
        change()
    else:
        print("Incorrect")

def main():
    ui()

if __name__ == "__main__":
    main()
