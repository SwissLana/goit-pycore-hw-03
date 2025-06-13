import re

def normalize_phone(phone_number):
    # Видалення всіх символів, крім цифр і '+'
    cleaned = re.sub(r'[^\d+]', '', phone_number.strip())

    # Якщо номер починається з '+380', залишаємо як є
    if cleaned.startswith('+380'):
        return cleaned

    # Якщо номер починається з '380', додаємо '+'
    if cleaned.startswith('380'):
        return '+' + cleaned

    # Якщо номер починається з '0', вважаємо, що це український номер і додаємо '+38'
    if cleaned.startswith('0'):
        return '+38' + cleaned

    # Якщо нічого з вищенаведеного, вважаємо, що це номер без коду країни
    return '+38' + cleaned

raw_phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

normalized_phone_numbers = [normalize_phone(num) for num in raw_phone_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", normalized_phone_numbers)  
