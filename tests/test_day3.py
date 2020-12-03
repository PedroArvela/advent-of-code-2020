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

def test_day3():
    matrix = prepare_input(INPUT)
    assert day3(matrix) == 7
