
contacts = {}

#додавання контакту
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."

# Функція для зміни контакту
def change_contact(args):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Контакт оновлено."
    else:
        return "Контакт не знайдено."

# Функція для отримання номера телефону
def phone(args):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Контакт не знайдено."

# Функція для виведення всіх контактів
def all():
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

# Парсер введення
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args