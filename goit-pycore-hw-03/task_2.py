import random

def get_numbers_ticket(min_num, max_num, quantity):
    """Генерує унікальні випадкові номери для лотерейного квитка."""
    # Перевіряємо, чи мінімальне і максимальне значення в межах від 1 до 1000
    if not 1 <= min_num <= max_num <= 1000:
        print("Параметри не відповідають заданим обмеженням. Оберіть числа від 1 до 1000.")
        return []
    # Перевіряємо, чи кількість чисел в межах від 1 до максимально можливого числа
    max_num_available = (max_num - min_num) + 1
    if quantity <=0 or quantity > max_num_available:
        print(f"Кількість чисел має бути від 1 до {max_num_available}" )
        return []
    # Генеруємо унікальні випадкові числа в межах від min_num до max_num включно
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    return sorted(numbers)

min_num = 98
max_num = 100
quantity = 3

ticket_numbers = get_numbers_ticket(min_num, max_num, quantity)
print("Ваші номери:", ticket_numbers)