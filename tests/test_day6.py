from day6.solution import prepare_input, day6_part1, day6_part2

INPUT = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""


def test_day6_part1():
    answers = prepare_input(INPUT)
    assert day6_part1(answers) == 11

def test_day6_part2():
    assert day6_part2(INPUT) == 6
