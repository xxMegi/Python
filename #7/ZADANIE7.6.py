import itertools
import random

# (a) Iterator zwracający 0, 1, 0, 1, 0, 1, ...
binary_iterator = itertools.cycle([0, 1])


# (b) Iterator zwracający przypadkowo jedną wartość z ("N", "E", "S", "W")
def random_directions():
    directions = ["N", "E", "S", "W"]
    while True:
        yield random.choice(directions)

random_direction_iterator = random_directions()

# (c) Iterator zwracający 0, 1, 2, ..., 6, 0, 1, 2, ..., 6 (dni tygodnia)
weekdays_iterator = itertools.cycle(range(7))


# Wyświetlenie wyników w konsoli - 10 przykładów
print("Iterator (a): ", [next(binary_iterator) for _ in range(10)])
print("\nIterator (b): ", [next(random_direction_iterator) for _ in range(10)])
print("\nIterator (c): ", [next(weekdays_iterator) for _ in range(10)])