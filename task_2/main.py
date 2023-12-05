import functions

def main():
    print("Вітаємо в боті-помічнику!")
    while True:
        user_input = input("Введіть команду: ")
        command, args = functions.parse_input(user_input)

        if command in ["close", "exit"]:
            print("До побачення!")
            break
        elif command == "hello":
            print("Як я можу вам допомогти?")
        elif command == "add":
            print(functions.add_contact(args))
        elif command == "change":
            print(functions.change_contact(args))
        elif command == "phone":
            print(functions.phone(args))
        elif command == "all":
            print(all())
        else:
            print("Невірна команда.")

if __name__ == "__main__":
    main()