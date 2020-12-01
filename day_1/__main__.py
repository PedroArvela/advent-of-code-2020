from typing import List
from solution import day1

def main():
    with open('inputs/day1.txt', 'r') as f:
        lines = f.read().splitlines()
        numbers = [int(l) for l in lines]
        print(day1(numbers))

if __name__ == "__main__":
    main()