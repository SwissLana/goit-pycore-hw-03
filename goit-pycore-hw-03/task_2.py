import random

def get_numbers_ticket(min_num, max_num, quantity):
    if not (1 <= min_num <= max_num <= 1000) or not (quantity == 8):
        print("Параметри не відповідають заданим обмеженням. Оберіть 8 чисел від 1 до 1000.")
        return []

    numbers = random.sample(range(min_num, max_num), quantity)
    return sorted(numbers)

min_num = 1
max_num = 1000
quantity = 8
ticket_numbers = get_numbers_ticket(min_num, max_num, quantity)
print("Ваші номери:", ticket_numbers)