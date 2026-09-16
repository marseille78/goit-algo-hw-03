import random

def get_numbers_ticket(min, max, quantity):
    if not isinstance(min, int) or not isinstance(max, int) or not isinstance(quantity, int):
        print("Аргументи мають бути цілими числами.")
        return;

    if min < 1 or max > 1000:
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

print(get_numbers_ticket(1, 49, 6))