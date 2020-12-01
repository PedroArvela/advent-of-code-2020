from typing import List

def day1(expense: List[int]) -> int:
    desired_sum = 2020

    for i, v1 in enumerate(expense):
        for v2 in expense[i:]:
            if v1 + v2 == desired_sum:
                return v1 * v2

    return -1


def main():
    with open('inputs/day1.txt', 'r') as f:
        lines = f.read().splitlines()
        numbers = [int(l) for l in lines]
        print(day1(numbers))

if __name__ == "__main__":
    main()