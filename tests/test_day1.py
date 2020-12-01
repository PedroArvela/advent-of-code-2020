from day_1 import day1

def test_day1():
    expense = [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]

    assert day1(expense) == 514579
