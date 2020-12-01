from typing import List

DESIRED_SUM = 2020

def day1(expense: List[int]) -> int:
    for i, v1 in enumerate(expense):
        for v2 in expense[i:]:
            if v1 + v2 == DESIRED_SUM:
                return v1 * v2

    return -1

def day1_part2(expense: List[int]) -> int:
    for i1, v1 in enumerate(expense):
        for i2, v2 in enumerate(expense[i1:]):
            for v3 in expense[i2:]:
                if v1 + v2 + v3 == DESIRED_SUM:
                    return v1 * v2 * v3
    
    return -1