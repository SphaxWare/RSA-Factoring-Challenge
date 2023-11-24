#!/usr/bin/python3
import sys
import time

def factorize(number):
    for i in range(2, number):
        if number % i == 0:
            return i, number // i
    return None, None

def main(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    for num in numbers:
        p, q = factorize(num)
        if p is not None and q is not None:
            print(f"{num}={p}*{q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    start_time = time.time()
    main(sys.argv[1])
    end_time = time.time()

    print(f"\nExecution time: {end_time - start_time:.3f} seconds")
