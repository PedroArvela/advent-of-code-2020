from day3.solution import day3, prepare_input

INPUT = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

def test_day3_1_1():
    matrix = prepare_input(INPUT)
    assert day3(matrix, 1, 1) == 2

def test_day3_3_1():
    matrix = prepare_input(INPUT)
    assert day3(matrix, 3, 1) == 7

def test_day3_5_1():
    matrix = prepare_input(INPUT)
    assert day3(matrix, 5, 1) == 3

def test_day3_7_1():
    matrix = prepare_input(INPUT)
    assert day3(matrix, 7, 1) == 4

def test_day3_1_2():
    matrix = prepare_input(INPUT)
    assert day3(matrix, 1, 2) == 2
