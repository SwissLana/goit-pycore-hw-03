from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    upcoming = []

    for user in users:
        # Перетворення дати народження у об'єкт datetime.date
        try:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except ValueError:
            continue  # Пропускаємо некоректні дати

        # Отримуємо дату народження цього року
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув цього року — беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Перевіряємо, чи потрапляє день народження у наступні 7 днів
        if today <= birthday_this_year <= end_date:
            congratulation_date = birthday_this_year

            # Якщо день народження припадає на вихідні — переносимо на наступний понеділок
            if congratulation_date.weekday() == 5:  # Субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # Неділя
                congratulation_date += timedelta(days=1)

            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming

users = [
    {"name": "Oleh Klymenko", "birthday": "1985.01.23"},
    {"name": "Olha Petriv", "birthday": "1990.05.27"},
    {"name": "Petro Ivanov", "birthday": "1992.06.20"},
    {"name": "Anna Bondar", "birthday": "1989.06.17"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)