import random

def get_numbers_ticket(min, max, quantity):
    if not isinstance(min, int) or not isinstance(max, int) or not isinstance(quantity, int):
        print("Аргументи мають бути цілими числами.")
        return;

    if min < 1 or max > 1000 or min >= max or quantity <= 0 or max - min < quantity:
        return []

    all_numbers = set()

    i = 0
    num = None

    while i < quantity:
        num = random.randint(min, max)

        if num in all_numbers:
            continue

        all_numbers.add(num)
        i += 1

    return sorted(list(all_numbers))

print("1: ", get_numbers_ticket(1, 49, 6))
print("2: ", get_numbers_ticket(-10, 10, 5))
print("3: ", get_numbers_ticket(1000, 1200, 10))
print("4: ", get_numbers_ticket(10, 4, 5))
print("5: ", get_numbers_ticket(10, 14, 6))