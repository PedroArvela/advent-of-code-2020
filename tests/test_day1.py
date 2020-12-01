from day_1 import day1, day1_part2

EXPENSE = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]

def test_day1():

    assert day1(EXPENSE) == 514579

def test_day1_part2():
    assert day1_part2(EXPENSE) == 241861950