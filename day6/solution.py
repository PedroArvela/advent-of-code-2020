import re
from typing import List, Set


def prepare_input(input: str) -> List[Set[str]]:
    group_strs = re.split(r'\n{2,}', input.strip())
    groups_answers = list()

    for group_str in group_strs:
        group_answers = set()
        for answer in group_str.splitlines():
            for c in answer:
                group_answers.add(c)
        
        groups_answers.append(group_answers)
        
    return groups_answers

def day6_part1(group_answers: List[Set[str]]) -> int:
    group_sum = 0

    for group in group_answers:
        group_sum += len(group)

    return group_sum

def day6_part2(input: str) -> int:
    group_strs = re.split(r'\n{2,}', input.strip())
    group_sum = 0

    for group_str in group_strs:
        group_count = len(group_str.splitlines())
        group_answer = dict()

        for answers in group_str.splitlines():
            for answer in answers:
                group_answer.setdefault(answer, 0)
                group_answer[answer] += 1

        all_positive = [a for a in group_answer if group_answer[a] == group_count]
        group_sum += len(all_positive)

    return group_sum
