from datetime import datetime


def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthdays = []

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days < 7:
            day_of_week = birthday_this_year.strftime('%A')
            if day_of_week in ['Saturday', 'Sunday']:
                day_of_week = 'Monday'
            birthdays.append((delta_days, day_of_week, name))

    birthdays.sort()

    for delta_days, day_of_week, name in birthdays:
        print(f"{day_of_week}: {name}")


users_input = input("Введіть дані користувачів: ")
users = eval(users_input)
get_birthdays_per_week(users)
