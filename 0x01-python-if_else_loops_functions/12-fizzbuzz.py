#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0:
            print("Fizz", end=' ')
        elif num % 5 == 0:
            print("Buzz", end=' ')
        elif num % 15 == 0:
            print("FizzBuzz", end=' ')
        print(f"{num:d}".format(num), end=' ')