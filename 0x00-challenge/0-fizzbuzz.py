#!/usr/bin/env python3

def fizzbuzz(n):
    """
    FizzBuzz function prints Fizz, Buzz, FizzBuzz or the number from 1 to n
    """

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')
    print()  # Add a newline after printing all numbers

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        fizzbuzz(int(sys.argv[1]))
    else:
        print("Usage: ./0-fizzbuzz.py <number>")

