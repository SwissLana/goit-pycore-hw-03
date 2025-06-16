from datetime import datetime

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - given_date
        return delta.days
    except ValueError:
        return "Неправильний формат дати або неіснуюча дата. Використовуйте формат 'РРРР-ММ-ДД'."

date_input = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")
days_difference = get_days_from_today(date_input)
print(f"Кількість днів від вказаної дати до сьогодні: {days_difference}")